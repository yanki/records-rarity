import json
import MySQLdb
import sys
import urlparse
import oauth2 as auth
# import ss1
from bottle import route, request, response, hook, \
    HTTPError, HTTPResponse, template, redirect, error
# from apiclient.discovery import build
from util.settings import *
from util.models import *
# from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.poolmanager import PoolManager

# import ssl
# from functools import wraps
# def sslwrap(func):
#     @wraps(func)
#     def bar(*args, **kw):
#         kw['ssl_version'] = ssl.PROTOCOL_TLSv1
#         return func(*args, **kw)
#     return bar

# ssl.wrap_socket = sslwrap(ssl.wrap_socket)

consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
request_token_url = REQUEST_TOKEN
authorize_url = AUTHORIZE
access_token_url = ACCESS_TOKEN

global request_token
global consumer

user_agent = 'records-rarity/1.0'

# class MyAdapter(HTTPAdapter):
#     def init_poolmanager(self, connections, maxsize, block=False):
#         self.poolmanager = PoolManager(num_pools=connections,
#                                         maxsize=maxsize,
#                                         block=block,
#                                         ss1_version=ss1.PROTOCOL_TLSv1)

@route('/', method='GET')
def index_page():
    doc = open('vinyls.txt')
    text = doc.read()
    vinyls = text.split('|')

    return template('index.tpl', vinyls=vinyls)

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
<<<<<<< HEAD
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
    return template('index.tpl', vinyls=None)
=======
            if index is 0:
                break
    resp, content = client.request('https://api.discogs.com/database/search?release_title=' + vinyl[0] + '&artist=' + vinyl[1] + '&format=vinyl',
            headers={'User-Agent': user_agent})
    content = json.loads(content)
    content = content['results'][0]
    artist = vinyl[1]
    tracklist = None
    if not isinstance(content['genre'], basestring):
        genre = str(content['genre'][0])
    else:
        genre = str(content['genre'])
        # genre = str(type(content['genre']))
    album = str(content['title'])
    rarity = 0.0
    art = str(content['thumb'])
    year = str(content['year'])
    items = [artist, tracklist, genre, album, rarity, art, year]
    InsertRecord(artist=items[0], tracklist=items[1], genre=items[2],
                album=items[3], rarity=items[4], art=items[5], year=items[6])

    return template('index.tpl', vinyls=items)

@route('/insertuser', method = 'POST')
def insert_user():	
    username = request.forms.get('user')
    password = request.forms.get('pass')
	Name = request.forms.get('Name')
	Pict = request.forms.get('PictureURL')
	email = request.forms.get('email')
	zipc = request.forms.get('zip')
	city = request.forms.get('city')
	state = request.forms.get('state')
	street = request.forms.get('street')
	rarity = 0
	#open connection
	connection = MySQLdb.connect (host = "localhost", port = 8082, user = "root", passwd = "9apple", db = "miyanki_records")
	#prepare a cursor object
	cursor = connection.cursor ()
	#form query
	#INSERT INTO table_name VALUES (value1,value2,value3,...);
	query = "INSERT INTO users VALUES ('" + username + "','" + password + "','" + Name + "','" + Pict + "','" + email + "'," + zipc + ",'" + city + "','" + state + "','" + street + "'," + str(rarity) + ");"
	#execute SQL query using execute()
	cursor.execute (query)
	#close cursor object
	cursor.close ()
	#close the connection	
	connection.close()


>>>>>>> b9a1e6db2b497dd77d5d523739ae7d1ce8488442
