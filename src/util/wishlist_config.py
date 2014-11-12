import mysql.connector
import sys
import random
from settings import *

#python wishlist_config.py username wishlist_title num_of_records

def returnrandom():
    randlist = [0]
    for i in range(1, 490):
        randlist.append(i)
    return random.sample(randlist, int(sys.argv[3]))

cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
cursor = cnx.cursor()

randV_IDS = returnrandom()
for i in range(0, len(randV_IDS)):
    add_btw = ("INSERT INTO belongs_to_wishlist "
                "(v_id, username, title) "
                "VALUES (%s, %s, %s)")
    data_btw = (randV_IDS[i], sys.argv[1], sys.argv[2])
    cursor.execute(add_btw, data_btw)
    cnx.commit()

cursor.close()
cnx.close()
