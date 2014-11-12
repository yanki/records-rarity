import json
import sys
import urlparse
import oauth2 as auth
from bottle import route, request, response, hook, \
    HTTPError, HTTPResponse, template, redirect, error
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

user_agent = 'records-rarity/1.0'


@route('/', method='GET')
def index_page():
    return template('index.tpl', iterate="no", vinyls="WHAT")

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
    return template('newuser.tpl', made="no")

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
    rarity = 0
    InsertUser(name=name, username=username, password=password, picture=pict,
        email=email, zipcode=zipc, city=city, state=state, street=street, rarity=rarity)
    return template('newuser.tpl', made="yes")

@route('/newwishlist', method='GET')
def new_wishlist():
    return template('newwishlist.tpl', made="no")

@route('/insertwishlist', method='POST')
def insert_wishlist():
    username = request.forms.get('username')
    wishlist = request.forms.get('wishlist')
    InsertWishlist(username=username, wishlist=wishlist)
    return template('newwishlist.tpl', made="yes")
