import mysql.connector
import sys
import random
from settings import *

#python insertRandUsers.py num_users_to_add

cnx = mysql.connector.connect(user='root', password='9apple',
            host='localhost', database='miyanki_records')
cursor = cnx.cursor()

fname = ['James','Robert','Michael','William','David','Charles','Linda','Barbara','Nancy','Helen']
lname = ['Lee','Smith','Jones','Brown','Davis','Miller','Wilson','Anderson','White','Martin']
cities = ['Clinton','Madison','Franklin','Washington','Chester','Marion','Greenville','Springfield','Georgetown','Salem']
states = ['SC','NC','VA','TN','GA','FL','MS','AL']
streets1 = ['First','Second','Third','Main','Oak','Pine','Maple','Elm']
streets2 = ['Avenue','Street','Boulevard','Road','Circle']
picture = "http://img2.wikia.nocookie.net/__cb20110427230528/spore/images/6/6c/Question-mark.png"
password = "hunter2"



def randname(counter):
    return fname[counter%10] + " " + lname[(counter + counter/len(lname))%10]

def randstreet():
    return str(random.randint(100,999)) + " " + streets1[random.randint(0,len(streets1)-1)] + " " + streets2[random.randint(0,len(streets2)-1)] 

for i in range(0, int(sys.argv[1])):
    add_user = ("INSERT INTO users "
                "(username, password, name, picture, email, zipcode, city, state, street) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    name = randname(i)
    username = name[0] + name.split()[1]
    email = username + "@gmail.com"
    state = states[random.randint(0,len(states)-1)]
    city = cities[random.randint(0,len(cities)-1)]
    data_user = (username, password, name, picture, email, random.randint(10000, 59999), city, state, randstreet())
    cursor.execute(add_user, data_user)
    cnx.commit()

cursor.close()
cnx.close()
