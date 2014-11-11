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
    doc = open('vinyls.txt')
    text = doc.read()
    vinyls = text.split('|')

    return template('index.tpl', vinyls=vinyls)

