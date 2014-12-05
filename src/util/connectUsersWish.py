import mysql.connector
import sys
import random
from settings import *

#python connectUsersWish.py
#adds 2 wishlists to each user, each containing 20 records

cnx = mysql.connector.connect(user='root', password='9apple',
            host='localhost', database='miyanki_records')
cursor = cnx.cursor()

#first retrieve list of usernames

cursor.execute("SELECT username FROM users;")
users = cursor.fetchall()

#retrieve all v_ids as well

cursor.execute("SELECT v_id FROM records;")
v_ids = cursor.fetchall()

#wishlist: title, username
#belongs_to_wishlist: v_id, username, title

add_wl = ("INSERT INTO wishlist "
          "(title, username) "
          "VALUES (%s, %s)")

add_btw = ("INSERT INTO belongs_to_wishlist "
          "(v_id, username, title) "
          "VALUES (%s, %s, %s)")

titles = ["Christmas Wishlist","Most Wanted"]

#for each user
for user in users:
    #add 2 wishlists for each person
    for i in range(0,2):

        #add a wishlist for this user

        title = titles[i]
        data_wl = (title, user[0])
        cursor.execute(add_wl, data_wl)
        cnx.commit()

        v_wl = random.sample(v_ids, 10)

        for v in v_wl:

            #add belongs_to_wishlist entry

            data_btw = (v[0], user[0], title)
            cursor.execute(add_btw, data_btw)
            cnx.commit()

cursor.close()
cnx.close()
