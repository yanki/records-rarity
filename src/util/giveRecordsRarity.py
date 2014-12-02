import sys
import mysql.connector
import random
from settings import *

#giveRecordsRarity gives a random rarity to all records in the database.

cnx = mysql.connector.connect(user='root', password='9apple',
        host='localhost', database='miyanki_records')
cursor = cnx.cursor()

#get all records, via v_id

cursor.execute("SELECT v_id FROM records;")
v_ids = cursor.fetchall()

for v in v_ids:
    randrarity = random.uniform(0,10)
    update = "UPDATE records SET rarity = %s WHERE v_id = %s;" % (randrarity, v[0])
    cursor.execute(update)
    cnx.commit()

cursor.close()
cnx.close()

