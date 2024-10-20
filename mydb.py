#pip install mysql
#pip install mysql Connector
# pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mk9745566815',

)

#prepare a cursor object
mycursor =  database.cursor()

#create  a database

mycursor.execute('CREATE DATABASE elderco ')

print('All Done!')
