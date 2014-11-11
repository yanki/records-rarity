import mysql.connector
from mysql.connector import errorcode
from settings import *


def InsertRecord(**args):
    cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
    cursor = cnx.cursor()
    add_record = ("INSERT INTO records "
                "(artist, tracklist, genre, album, rarity, art, year) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    data_record = (args['artist'], args['tracklist'], args['genre'],
                args['album'], args['rarity'], args['art'], args['year'])
    cursor.execute(add_record, data_record)
    cnx.commit()
    cursor.close()
    cnx.close()
