import os
import json
import sys
import csv
import io
import httplib2
import urlparse
import oauth2 as auth
from bottle import route, request, response, hook, \
    HTTPError, HTTPResponse, template, redirect, error
# from apiclient.discovery import build
from util.settings import *


consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
request_token_url = REQUEST_TOKEN
authorize_url = AUTHORIZE
access_token_url = ACCESS_TOKEN
# auth_verifier = APP_CODE

global request_token
global consumer

user_agent = 'records-rarity/1.0'

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
    doc = open('vinyls.txt')
    text = doc.read()
    vinyls = text.split('|')
    resp, content = client.request('https://api.discogs.com/database/search?release_title=' + vinyls[0] + '&artist=' + vinyls[1] + '&format=vinyl',
            headers={'User-Agent': user_agent})
    # resp, content = client.request('https://api.discogs.com/database/search?title=Nirvana%20-%20Nevermind&format=vinyl',
    #         headers={'User-Agent': user_agent})
    # vinyls.append(access_token['oauth_token'])
    # vinyls.append(access_token['oauth_token_secret'])

    return template('index.tpl', vinyls=content)
