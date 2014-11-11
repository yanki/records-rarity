#!/usr/bin/python

#python script to retrieve a single row

#import MySQL Db and sys modules
import MySQLdb
import sys

#open connection

connection = MySQLdb.connect (host = "localhost",port = 8082, user = "root", passwd = "9apple", db = "miyanki_records")

#prepare a cursor object

cursor = connection.cursor ()

#execute SQL query using execute()

cursor.execute ("SELECT RECORDS()")

#fetch a single row

row = cursor.fetchone ()

#print row
print "Server version:",row[0]

#close cursor object
cursor.close ()

#close the connection

connection.close()

#exit the program
sys.exit ()
