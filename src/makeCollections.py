#!/usr/bin/python

#python script to give a user a random number of vinyls in their owned vinyl
#python script
#import MySQL Db and sys modules
import MySQLdb
import sys
import random

def returnrandom():
	randlist = [0]
	for i in range(1,0):
		randlist.append(i)
	return random.sample(randlist, sys.argv[2])

#open connection

connection = MySQLdb.connect (host = "localhost", port = 8082, user = "root", passwd = "9apple", db = "miyanki_records")

#prepare a cursor object

cursor = connection.cursor()

#first get a record of all vinyls in the database

cursor.execute("SELECT v_id FROM records;")
records = cursor.fetchall()
o_id = sys.argv[3] + 1
conditions = ['Acceptable','Good','Very Good','Like New','Brand New']

#owned_vinyl: o_id,'quality',price,tradable,sellable,'username'
#described_by: v_id,o_id


randV_IDS = returnrandom()
for i in range(0, len(randV_IDS)):
	cursor.execute("INSERT INTO owned_vinyl VALUES (" + str(o_id) + ",'" + conditions[random.randint(0,4)] + "'," + "{0:.2f}".format(random.randuniform(0,101)) + "," + str(random.randint(0,1)) + "," + str(random.randint(0,1)) + "," + sys.argv[1] + ");")
	cursor.execute("INSERT INTO described_by VALUES (" + str(randV_IDS[i]) + "," + str(o_id) + ");")
	o_id = o_id + 1

#close cursor object
cursor.close ()

#close the connection

connection.close()

#exit the program
sys.exit ()

