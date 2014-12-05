import json
import sys
import urlparse
import oauth2 as auth
from bottle import route, request, response, hook, \
    HTTPError, HTTPResponse, template, redirect, error
# from request import args
# from apiclient.discovery import build
from util.settings import *
from util.models import *
# from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.poolmanager import PoolManager

consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
request_token_url = REQUEST_TOKEN
authorize_url = AUTHORIZE
access_token_url = ACCESS_TOKEN

global request_token
global consumer

user_details = {}
wishlists = []
wishlist_inuse = None
search_items = []

user_agent = 'records-rarity/1.0'


@route('/', method='GET')
def index_page():
    return template('index.tpl', error="no")

@route('/token')
def get_token():
    global request_token
    global consumer

    consumer = auth.Consumer(consumer_key, consumer_secret)
    client = auth.Client(consumer)
    resp, content = client.request(request_token_url, 'POST', headers={'User-Agent': user_agent})
    if resp['status'] != '200':
        sys.exit('Invalid response {0}.'.format(resp['status']))
    request_token = dict(urlparse.parse_qsl(content))
    url = ('{0}?oauth_token={1}'.format(authorize_url, request_token['oauth_token']))
    return template('token.tpl', url=url)

@route('/auth', method='POST')
def finish_authenticate():
    global request_token
    global consumer

    auth_verifier = request.forms.get('code')
    token = auth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
    token.set_verifier(auth_verifier)
    client = auth.Client(consumer, token)
    resp, content = client.request(access_token_url, 'POST', headers={'User-Agent': user_agent})
    access_token = dict(urlparse.parse_qsl(content))
    token = auth.Token(key=access_token['oauth_token'],
            secret=access_token['oauth_token_secret'])
    client = auth.Client(consumer, token)
    with open('vinyls.txt') as f:
        for index, line in enumerate(f):
            line = line.rstrip()
            vinyl = line.split('|')
            resp, content = client.request('https://api.discogs.com/database/search?release_title=' + vinyl[0] + '&artist=' + vinyl[1] + '&format=vinyl',
                            headers={'User-Agent': user_agent})
            content = json.loads(content)
            if 'results' in content.keys() and len(content['results']) > 0:
                # break
                content = content['results'][0]
                title = content['title'].split(' - ')
                artist = title[0].encode('utf-8')
                tracklist = None
                if not isinstance(content['genre'], basestring):
                    genre = str(content['genre'][0])
                else:
                    genre = str(content['genre'])
                album = title[1].encode('utf-8')
                rarity = 0.0
                art = str(content['thumb'])
                if 'year' in content.keys():
                    year = str(content['year'])
                else:
                    year = '0000'
                items = [artist, tracklist, genre, album, rarity, art, year]
                InsertRecord(artist=items[0], tracklist=items[1], genre=items[2],
                            album=items[3], rarity=items[4], art=items[5], year=items[6])
                # out[artist] = album
                if index is 100:
                    break
            else:
                continue
    return template('index.tpl', vinyls=None, iterate="yes")

@route('/newuser', method='GET')
def new_user():
    return template('newuser.tpl', info=None)

@route('/insertuser', method='POST')
def insert_user():
    username = request.forms.get('username')
    password = request.forms.get('password')
    name = request.forms.get('name')
    pict = None
    email = request.forms.get('email')
    zipc = request.forms.get('zip')
    city = request.forms.get('city')
    state = request.forms.get('state')
    street = request.forms.get('street')
    rarity = 0.0
    InsertUser(name=name, username=username, password=password, picture=pict,
        email=email, zipcode=zipc, city=city, state=state, street=street, rarity=rarity)
    return template('index.tpl', error="success")

@route('/updateuser', method='POST')
def insert_user():
    global user_details
    password = request.forms.get('password')
    name = request.forms.get('name')
    pict = None
    email = request.forms.get('email')
    zipc = request.forms.get('zip')
    city = request.forms.get('city')
    state = request.forms.get('state')
    street = request.forms.get('street')
    user_details['password'] = password
    user_details['name'] = name
    user_details['email'] = email
    user_details['zipcode'] = zipc
    user_details['city'] = city
    user_details['state'] = state
    user_details['street'] = street
    UpdateUser(name=name, username=None, password=password, picture=pict,
        email=email, zipcode=zipc, city=city, state=state, street=street)
    return template('homepage.tpl', details=user_details, contents=None, type="update")

@route('/newwishlist', method='GET')
def new_wishlist():
    return template('newwishlist.tpl', made="no")

@route('/insertwishlist', method='POST')
def insert_wishlist():
    username = request.forms.get('username')
    wishlist = request.forms.get('wishlist')
    InsertWishlist(username=username, wishlist=wishlist)
    return template('newwishlist.tpl', made="yes")

@route('/login', method='POST')
def login():
    global user_details

    username = request.forms.get('username')
    password = request.forms.get('password')
    GenerateRarity(username=username)
    details = getUser(username=username, password=password)
    if details is False:
        return template('index.tpl', error="yes")
    else:
        user_details = details
        return template('homepage.tpl', details=user_details, contents=None)

@route('/login', method='GET')
def reLogin():
    global user_details

    if len(user_details) < 1:
        return template('index.tpl', error="yes")
    else:
        return template('homepage.tpl', details=user_details, contents=None)

@route('/owned', method='GET')
def records():
    global user_details

    records = getRecords(username=user_details['username'])
    return template('homepage.tpl', details=user_details, contents=[records, None, None], type="records")

@route('/wishlists', method='GET')
def wishlists():
    global user_details
    global wishlists

    wishlists = getWishlists(username=user_details['username'])
    return template('homepage.tpl', details=user_details, contents=[wishlists, None, None], type="wishlists")

@route('/newwish', method="POST")
def makewish():
    global user_details
    global wishlists
    wish = request.forms.get('wish')
    InsertWishlist(username=user_details['username'], wishlist=wish)
    wishlists.append([(wish,)])
    return template('homepage.tpl', details=user_details, contents=[wishlists, None, None], type="wishlists")

@route('/getwish', method="POST")
def getwish():
    global user_details
    global wishlists
    global wishlist_inuse

    wishlist = request.forms.get('wishname')
    wishes = getWishes(wishlist=wishlist, username=user_details['username'])
    contents = [wishlists, wishes, wishlist]
    wishlist_inuse = wishlist
    return template('homepage.tpl', details=user_details, contents=contents, type="wishlists")

@route('/findowners', method="POST")
def findowners():
    global user_details

    record = request.forms.get('albumname')
    owners = getOwners(album=record, username=user_details['username'])
    contents = [owners, record]
    return template('homepage.tpl', details=user_details, contents=contents, type="owners")

@route('/deleterecord', method="POST")
def deleteRecord():
    o_id = request.forms.get('delete')
    deleteEntry(value=o_id, table="owned_vinyl", attr="o_id", type="record")
    records = getRecords(username=user_details['username'])
    return template('homepage.tpl', details=user_details, contents=[records, True, None], type="records")

@route('/deletewish', method="POST")
def deleteWish():
    global wishlist_inuse
    global user_details
    global wishlists

    v_id = request.forms.get('delete')
    deleteEntry(value=v_id, table="belongs_to_wishlist", attr="v_id", username=user_details['username'], title=wishlist_inuse, type="wish")
    wishes = getWishes(wishlist=wishlist_inuse, username=user_details['username'])
    contents = [wishlists, wishes, wishlist_inuse]
    return template('homepage.tpl', details=user_details, contents=contents, type="wishlists")

@route('/removewishlist', method="POST")
def removeWishlist():
    global user_details
    global wishlists

    title = request.forms.get('wishname')
    deleteEntry(value=title, table="wishlist", attr="title", username=user_details['username'], type='list')
    wishlists = getWishlists(username=user_details['username'])
    return template('homepage.tpl', details=user_details, contents=[wishlists, None, None], type="wishlists")


@route('/editinfo', method="GET")
def editInfo():
    global user_details
    return template('newuser.tpl', info=user_details)

@route('/search', method="POST")
def search():
    global search_items
    items = (request.forms.get('items')).split(' ')
    search_items = items
    print search_items
    results = SearchResults(items=items)
    return template('homepage.tpl', details=user_details, contents=[results, "Search results for " + ' '.join(items), None], type="search")

@route('/ownrecord', method="POST")
def addRecord():
    global user_details
    global search_items
    kind = request.forms.get('type')
    v_id = request.forms.get('v_id')
    if kind == "details":
        return template('add.tpl', type="own", v_id=v_id)
    elif kind == "add":
        quality = request.forms.get('quality')
        price = request.forms.get('price')
        trade = request.forms.get('trade')
        sell = request.forms.get('sell')
        AddRecord(username=user_details['username'], v_id=v_id, quality=quality, price=price, trade=trade, sell=sell)
        results = SearchResults(items=search_items)
        return template('homepage.tpl', details=user_details, contents=[results, "Search results for " + ' '.join(search_items), None], type="search")

@route('/ownwish', method="POST")
def addWish():
    global user_details
    global search_items
    kind = request.forms.get('type')
    v_id = request.forms.get('v_id')
    if kind == "details":
        wishlists = getWishlists(username=user_details['username'])
        return template('add.tpl', type="wish", v_id=v_id, wishlists=wishlists)
    elif kind == "add":
        title = request.forms.get('wishlist')
        AddWish(username=user_details['username'], v_id=v_id, title=title)
        results = SearchResults(items=search_items)
        return template('homepage.tpl', details=user_details, contents=[results, "Search results for " + ' '.join(search_items), None], type="search")
