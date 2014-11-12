import mysql.connector
import sys
import random
from settings import *

conditions = ['Acceptable', 'Good', 'Very Good', 'Like New', 'Brand New'] 

def returnrandom():
    randlist = [0]
    for i in range(1, 490):
        randlist.append(i)
    return random.sample(randlist, int(sys.argv[2]))

cnx = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASS,
            host=DATABASE_LOCATION, database=DATABASE_NAME)
cursor = cnx.cursor()

o_id = int(sys.argv[3]) + 1

randV_IDS = returnrandom()
for i in range(0, len(randV_IDS)):
    add_owned = ("INSERT INTO owned_vinyl "
                "(o_id, quality, price, tradable, sellable, username) "
                "VALUES (%s, %s, %s, %s, %s, %s)")
    data_owned = (o_id, conditions[random.randint(0, 4)], "{0:.2f}".format(random.uniform(0, 101)), random.randint(0, 1), random.randint(0, 1), sys.argv[1])
    cursor.execute(add_owned, data_owned)
    cnx.commit()
    add_desc = ("INSERT INTO described_by "
                "(v_id, o_id) "
                "VALUES (%s, %s)")
    data_desc = (randV_IDS[i], o_id)
    cursor.execute(add_desc, data_desc)
    cnx.commit()
    o_id += 1
cursor.close()
cnx.close()
