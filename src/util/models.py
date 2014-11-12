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

def InsertUser(**args):
    cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
    cursor = cnx.cursor()
    add_user = ("INSERT INTO users "
                "(username, password, name, picture, email, zipcode, city, state, street, rarity) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    data_user = (args['username'], args['password'], args['name'],
                args['picture'], args['email'], args['zipcode'], args['city'], args['state'], args['street'], args['rarity'])
    cursor.execute(add_user, data_user)
    cnx.commit()
    cursor.close()
    cnx.close()
