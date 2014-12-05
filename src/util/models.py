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

def UpdateUser(**args):
    cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
    cursor = cnx.cursor()
    add_user = ("UPDATE users SET "
                "name=%s, password=%s, email=%s, zipcode=%s, city=%s, state=%s, street=%s "
                "WHERE username=%s;")
    data_user = (args['name'], args['password'], args['email'],
                args['zipcode'], args['city'], args['state'], args['street'], args['username'])
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

def getUser(**args):
    cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
    cursor = cnx.cursor()
    cursor.execute("SELECT COUNT(1) FROM users WHERE username=%s AND password=%s", (args['username'], args['password']))
    if cursor.fetchone()[0]:
        details = {}
        cursor.execute("SELECT username, name, picture, email, zipcode, city, state, street, rarity, password FROM users WHERE username=%s AND password=%s", (args['username'], args['password']))
        for (username, name, picture, email, zipcode, city, state, street, rarity, password) in cursor:
            details['username'] = username
            details['name'] = name
            details['email'] = email
            details['zipcode'] = zipcode
            details['city'] = city
            details['state'] = state
            details['street'] = street
            details['rarity'] = rarity
            details['picture'] = picture
            details['password'] = password
        cursor.close()
        cnx.close()
        return details
    else:
        cursor.close()
        cnx.close()
        return False

def getRecords(**args):
    cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
    cursor = cnx.cursor()
    query = "SELECT owned_vinyl.o_id, records.artist, records.album, records.genre, records.year, records.rarity FROM records, described_by, owned_vinyl WHERE owned_vinyl.username='%s' AND owned_vinyl.o_id=described_by.o_id AND described_by.v_id=records.v_id ORDER BY records.artist;" % (args['username'])
    cursor.execute(query)
    contents = []
    for (num, artist, album, genre, year, rarity) in cursor:
        contents.append([num, artist, album, genre, year, rarity])
    cursor.close()
    cnx.close()
    return contents

def SearchResults(**args):
    cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
    cursor = cnx.cursor()
    query = "SELECT records.v_id, records.artist, records.album, records.genre, records.year, records.rarity FROM records WHERE "
    for index, word in enumerate(args['items']):
        if index > 0:
            query += "OR (Concat(artist, '', album, '', year, '', genre) like '%" + word + "%') "
        else:
            query += "(Concat(artist, '', album, '', year, '', genre) like '%" + word + "%') "
    query += "ORDER BY records.artist;"
    cursor.execute(query)
    contents = []
    for (num, artist, album, genre, year, rarity) in cursor:
        contents.append([num, artist, album, genre, year, rarity])
    cursor.close()
    cnx.close()
    return contents

def getWishlists(**args):
    cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
    cursor = cnx.cursor()
    query = "SELECT title FROM wishlist WHERE username='%s' ORDER BY title;" % (args['username'])
    cursor.execute(query)
    contents = []
    for (title) in cursor:
        contents.append([title])
    cursor.close()
    cnx.close()
    return contents

def getWishes(**args):
    cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
    cursor = cnx.cursor()
    query = "SELECT records.v_id, records.artist, records.album, records.year FROM records, belongs_to_wishlist WHERE belongs_to_wishlist.username='%s' AND belongs_to_wishlist.title='%s' AND records.v_id=belongs_to_wishlist.v_id ORDER BY records.artist;" % (args['username'], args['wishlist'])
    cursor.execute(query)
    contents = []
    for (v_id, artist, album, year) in cursor:
        contents.append([v_id, artist, year, album])
    cursor.close()
    cnx.close()
    return contents

def getOwners(**args):
    cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
    cursor = cnx.cursor()
    query = ("SELECT users.username, users.name, users.email, users.zipcode, users.city, users.state, users.street, "
        "owned_vinyl.quality, owned_vinyl.price, owned_vinyl.tradable, owned_vinyl.sellable "
        "FROM users, records, described_by, owned_vinyl WHERE records.album='%s' AND records.v_id=described_by.v_id "
        "AND described_by.o_id=owned_vinyl.o_id AND owned_vinyl.username!='%s' AND (owned_vinyl.tradable='1' OR owned_vinyl.sellable='1') "
        "AND users.username=owned_vinyl.username "
        "ORDER BY price;" % (args['album'], args['username']))
    cursor.execute(query)
    contents = []
    for (username, name, email, zipcode, city, state, street, quality, price, trade, sell) in cursor:
        contents.append([username, name, email, zipcode, city, state, street, quality, price, trade, sell])
    cursor.close()
    cnx.close()
    return contents

def deleteEntry(**args):
    cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
    cursor = cnx.cursor()
    if args['type'] is "record":
        query = "DELETE FROM %s WHERE %s='%s';" % (args['table'], args['attr'], args['value'])
    elif args['type'] is "wish":
        query = "DELETE FROM %s WHERE %s='%s' AND username='%s' AND title='%s';" % (args['table'], args['attr'], args['value'], args['username'], args['title'])
    elif args['type'] is "list":
        query = "DELETE FROM %s WHERE %s='%s' AND username='%s';" % (args['table'], args['attr'], args['value'], args['username'])
        print query
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True

def AddRecord(**args):
    cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
    cursor = cnx.cursor()
    if args['sell'] == "on":
        sell = 1
    else:
        sell = 0
    if args['trade'] == "on":
        trade = 1
    else:
        trade = 0
    query = "INSERT INTO owned_vinyl (quality, price, tradable, sellable, username) VALUES('%s', %s, %s, %s, '%s');" % (args['quality'], args['price'], trade, sell, args['username'])
    cursor.execute(query)
    query = "SELECT LAST_INSERT_ID();"
    cursor.execute(query)
    for o_id in cursor:
        query = "INSERT INTO described_by (v_id, o_id) VALUES(%s, %s);" % (args['v_id'], o_id[0])
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True

def AddWish(**args):
    cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
    cursor = cnx.cursor()
    query = "INSERT INTO belongs_to_wishlist (v_id, username, title) VALUES(%s, '%s', '%s');" % (args['v_id'], args['username'], args['title'])
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True

def GenerateRarity(**args):
    cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
    cursor = cnx.cursor()

    query = "SELECT AVG(records.rarity) FROM records,owned_vinyl,described_by WHERE owned_vinyl.username = '%s' AND owned_vinyl.o_id = described_by.o_id AND records.v_id = described_by.v_id;" % (args['username'])
    cursor.execute(query)
    avg = cursor.fetchall()[0][0]
    update = "UPDATE users SET rarity = %s WHERE username = '%s';" % ("{0:.1f}".format(avg), args['username'])
    cursor.execute(update)
    cnx.commit()

    cursor.close()
    cnx.close()
