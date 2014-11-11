import os
import json
import csv
import io
import httplib2
from bottle import route, request, response, hook, \
    HTTPError, HTTPResponse, template, redirect, error
# from apiclient.discovery import build
from util.settings import *


@route('/', method='GET')
def index_page():
    return template('index.tpl')

