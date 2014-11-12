import mysql.connector
from mysql.connector import errorcode
from settings import *
from util.models import *


fh = open("info.txt","r")
	for line in fh:
		rank, album, artist, year, genre = line.split("|")
		InsertRecord(artist=artist, tracklist=None, genre=genre, 
			album=album, rarity=None, art=None, year=year)
fh.close()
