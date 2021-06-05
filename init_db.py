import sqlite3

conn = sqlite3.connect('database.db')
print( "Opened database successfully")

conn.execute('CREATE TABLE stackoverflow (topic TEXT, votes INTEGER, answers INTEGER, views INTEGER, title TEXT, link TEXT, subtitle TEXT, date INTEGER, user TEXT, avatar TEXT,userlink TEXT, querydate INTEGER, starred INTEGER, notes TEXT, read INTEGER, rank INTEGER)')
print("Table created successfully")
conn.close()