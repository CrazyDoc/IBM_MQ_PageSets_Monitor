import sqlite3
from sqlite3 import Error
import time
import os
os.environ["SETTINGS_MODULE"] = 'settings'
from python_settings import settings

table_name = 'ps' + str(int(int(time.time()) / 86400))


def connection(database):
	try:
		con = sqlite3.connect(database)
		return con
	except Error:
		print(Error)


def create_table(con, table_name):
	cursorObj = con.cursor()
	cursorObj.execute(
		"CREATE TABLE if not exists " + table_name + "(id integer PRIMARY KEY AUTOINCREMENT, label text, timestamp integer, percent integer)")
	con.commit()


def listing_table(con):
	listing_table = []
	cursorObj = con.cursor()
	if cursorObj.execute('SELECT name from sqlite_master where type= "table"') == 0:
		print('have no table')
	else:
		for string in cursorObj:
			listing_table.append(string[0])
	print(listing_table)
	return(listing_table)


def insert(con, table_name, data):
	cursorObj = con.cursor()
	create_table(con, table_name)
	#	data = [(label, timestamp, percent)]
	cursorObj.executemany("INSERT INTO " + table_name + " (label, timestamp, percent) VALUES(?, ?, ?)", data)
	con.commit()


def listing_rows(con):
	listing_row = []
	cursorObj = con.cursor()
	if cursorObj.execute('SELECT * FROM ' + table_name) == 0:
		print('have no table')
	else:
		for string in cursorObj:
			listing_row.append(string)
	print(listing_row)
	return(listing_row)


def del_table(con, table_name):
	cursorObj = con.cursor()
	cursorObj.execute('DROP table if exists ' + table_name)
	con.commit()


def drop_table(con, table_name):
	cursorObj = con.cursor()
	try:
		cursorObj.execute('DROP table if exists ' + table_name)
		con.commit()
		print('table ' + table_name + ' deleted')
	except:
		print('table ' + table_name + ' not deleted')


#con = connection(settings.DATABASE)

#create_table(con, table_name)

#listing_table(con)

#listing_rows(con)

#insert(con, table_name, [('PS0', int(time.time()), int(80))])

#for i in listing_table(con): drop_table(con, i)


#con.close()
