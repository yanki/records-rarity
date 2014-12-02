import mysql.connector
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

def InsertWishlist(**args):
    cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
    cursor = cnx.cursor()
    add_wish = ("INSERT INTO wishlist "
                "(title, username) "
                "VALUES (%s, %s)")
    data_wish = (args['wishlist'], args['username'])
    cursor.execute(add_wish, data_wish)
    cnx.commit()
    cursor.close()
    cnx.close()

def SearchRecords(**args):
    cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
    cursor = cnx.cursor()

    search_string = args['search_field'] #change to whatever the form is
    search_result = set()

    for s in search_string.split():
        query = "SELECT DISTINCT artist,album,genre,year FROM records WHERE\
 artist LIKE '%" + s + "%' OR album LIKE '%" + s + "%'"
        cursor.execute(query)
        data = cursor.fetchall()
        for d in data:
            search_result.add(d) 

    #do something with search_result

    cursor.close()
    cnx.close()

def GenerateRarity(**args):
    cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
    cursor = cnx.cursor()

    query = "SELECT AVG(records.rarity) FROM records,owned_vinyl,described_by WHERE owned_vinyl.username = '%s' AND owned_vinyl.o_id = described_by.o_id AND records.v_id = described_by.v_id;" % (args['username'])
    cursor.execute(query)
    avg = cursor.fetchall()[0][0]
    
    update = "UPDATE users SET rarity = %s WHERE username = '%s';" % (avg, args['username'])
    cursor.execute(update)
    cnx.commit()

    cursor.close()
    cnx.close()

