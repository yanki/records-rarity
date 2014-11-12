from __future__ import print_function
import mysql.connector as connector
from mysql.connector import errorcode

DB_NAME = 'miyanki_records'

TABLES = {}
RELATIONS = {}
TABLES['belongs_to_wishlist'] = (
    "CREATE TABLE IF NOT EXISTS `belongs_to_wishlist` ("
    "`v_id` int(10) NOT NULL,"
    "`username` varchar(10) NOT NULL,"
    "`title` varchar(500) NOT NULL,"
    "PRIMARY KEY (`v_id`,`username`,`title`),"
    "KEY `username` (`username`),"
    "KEY `title` (`title`)"
    ") ENGINE=InnoDB DEFAULT CHARSET=latin1;")
TABLES['described_by'] = (
    "CREATE TABLE IF NOT EXISTS `described_by` ("
    "`v_id` int(11) NOT NULL,"
    "`o_id` int(11) NOT NULL,"
    "PRIMARY KEY (`v_id`,`o_id`),"
    "KEY `o_id` (`o_id`)"
    ") ENGINE=InnoDB DEFAULT CHARSET=latin1;")
TABLES['owned_vinyl'] = (
    "CREATE TABLE IF NOT EXISTS `owned_vinyl` ("
    "`o_id` int(11) NOT NULL AUTO_INCREMENT,"
    "`quality` varchar(30) DEFAULT NULL,"
    "`price` float DEFAULT NULL,"
    "`tradable` tinyint(1) NOT NULL,"
    "`sellable` tinyint(1) NOT NULL,"
    "`username` varchar(10) NOT NULL,"
    "PRIMARY KEY (`o_id`),"
    "KEY `username` (`username`)"
    ") ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1;")
TABLES['records'] = (
    "CREATE TABLE IF NOT EXISTS `records` ("
    "`v_id` int(10) NOT NULL AUTO_INCREMENT,"
    "`artist` varchar(500) NOT NULL,"
    "`tracklist` varchar(5000) DEFAULT NULL,"
    "`genre` varchar(500) DEFAULT NULL,"
    "`album` varchar(500) NOT NULL,"
    "`rarity` double NOT NULL,"
    "`art` varchar(500) DEFAULT NULL,"
    "`year` int(4) NOT NULL,"
    "PRIMARY KEY (`v_id`)"
    ") ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1;")
TABLES['users'] = (
    "CREATE TABLE IF NOT EXISTS `users` ("
    "`username` varchar(10) NOT NULL,"
    "`password` varchar(30) NOT NULL,"
    "`name` varchar(500) DEFAULT NULL,"
    "`picture` varchar(500) DEFAULT NULL,"
    "`email` varchar(500) DEFAULT NULL,"
    "`zipcode` int(5) unsigned DEFAULT NULL,"
    "`city` varchar(500) DEFAULT NULL,"
    "`state` varchar(2) DEFAULT NULL,"
    "`street` varchar(500) DEFAULT NULL,"
    "`rarity` int(10) unsigned DEFAULT NULL,"
    "PRIMARY KEY (`username`)"
    ") ENGINE=InnoDB DEFAULT CHARSET=latin1;")
TABLES['wishlist'] = (
    "CREATE TABLE IF NOT EXISTS `wishlist` ("
    "`title` varchar(500) NOT NULL,"
    "`username` varchar(10) NOT NULL,"
    "PRIMARY KEY (`title`,`username`),"
    "KEY `username` (`username`)"
    ") ENGINE=InnoDB DEFAULT CHARSET=latin1;")
RELATIONS['belongs_to_wishlist'] = (
    "ALTER TABLE `belongs_to_wishlist`"
    "ADD CONSTRAINT `belongs_to_wishlist_ibfk_3` FOREIGN KEY (`v_id`) REFERENCES `records` (`v_id`) ON DELETE CASCADE ON UPDATE CASCADE,"
    "ADD CONSTRAINT `belongs_to_wishlist_ibfk_1` FOREIGN KEY (`username`) REFERENCES `wishlist` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,"
    "ADD CONSTRAINT `belongs_to_wishlist_ibfk_2` FOREIGN KEY (`title`) REFERENCES `wishlist` (`title`) ON DELETE CASCADE ON UPDATE CASCADE;")
RELATIONS['described_by'] = (
    "ALTER TABLE `described_by`"
    "ADD CONSTRAINT `described_by_ibfk_3` FOREIGN KEY (`o_id`) REFERENCES `owned_vinyl` (`o_id`) ON DELETE CASCADE ON UPDATE CASCADE,"
    "ADD CONSTRAINT `described_by_ibfk_1` FOREIGN KEY (`v_id`) REFERENCES `records` (`v_id`) ON DELETE CASCADE ON UPDATE CASCADE;")
RELATIONS['owned_vinyl'] = (
    "ALTER TABLE `owned_vinyl`"
    "ADD CONSTRAINT `owned_vinyl_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;")
RELATIONS['wishlist'] = (
    "ALTER TABLE `wishlist`"
    "ADD CONSTRAINT `wishlist_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE NO ACTION;")

cnx = connector.connect(user='root', password='yanmik1023')
cursor = cnx.cursor()


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME
except connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for name, dd1 in TABLES.iteritems():
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(dd1)
    except connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
for name, dd1 in RELATIONS.iteritems():
    try:
        print("Altering table {}: ".format(name), end='')
        cursor.execute(dd1)
    except connector.Error as err:
        print(err.msg)
    else:
        print("OK")
cursor.close()
cnx.close()
