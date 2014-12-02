import mysql.connector
import sys
import random
from settings import *

#python connectUsersVinyl.py
#automatically adds 50 vinyls to each user's owned vinyls collection

cnx = mysql.connector.connect(user='root', password='9apple',
            host='localhost', database='miyanki_records')
cursor = cnx.cursor()

#first retrieve list of usernames

cursor.execute("SELECT username FROM users;")
users = cursor.fetchall()

#retrieve all v_ids as well

cursor.execute("SELECT v_id FROM records;")
v_ids = cursor.fetchall()

#owned_vinyl: o_id, quality, price, tradable, sellable, username
#described_by: o_id, v_id


qualities = ["Brand New","Like New","Very Good","Good","Acceptable"]

#get starting o_id

cursor.execute("SELECT COUNT(*) FROM owned_vinyl;")
o_id = cursor.fetchall()[0][0]+1

add_ov = ("INSERT INTO owned_vinyl "
          "(o_id, quality, price, tradable, sellable, username) "
          "VALUES (%s, %s, %s, %s, %s, %s)")

add_db = ("INSERT INTO described_by "
          "(o_id, v_id) "
          "VALUES (%s, %s)")

#for each user
for user in users:
    #add 50 owned vinyls
    for i in range(0,50):

        #add owned vinyl entry

        quality = qualities[random.randint(0,len(qualities)-1)]
        price = "%0.2f" % (random.uniform(0,100),)
        data_ov = (o_id, quality, price, random.randint(0,1), random.randint(0,1), user[0])
        cursor.execute(add_ov, data_ov)
        cnx.commit()

        #add described_by entry
    
        data_db = (o_id, v_ids[random.randint(0,len(v_ids)-1)][0])
        cursor.execute(add_db, data_db)
        cnx.commit()

        o_id += 1

cursor.close()
cnx.close()
