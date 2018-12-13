import datetime
import mysql.connector as mysql
from mysql.connector import errorcode

#set PYTHONPATH=src
import os, sys
path=os.path.abspath(__file__)
fd=os.path.dirname(path)
directoryName=os.path.dirname(fd)
sys.path.append(directoryName)

db_master = 'mindgame_db'
db_host='134.173.236.104'
db_user='mindgame'
db_password='password'
db_table=''

def open_test_close():
    try:
        connection=mysql.connect(user=db_user,password=db_password, host=db_host, database=db_master)
        print("connection opened_open_test_close")
    except mysql.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    else:
        connection.close()
        print ('Connection Closed_open_test_close')
open_test_close()

def openDB():
    try:
        connection=mysql.connect(user=db_user,password=db_password, host=db_host, database=db_master)
        print("connection opened")
        return connection
    except mysql.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            return err
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            return err
        else:
            print(err)
            return err

def CloseDB():
    pass
# print ('should be closing')
# c = cnx.cursor()
# c.close()
# cnx.close()
# if cnx.close() == None:
# print('Connection Closed')
# return cnx

def write_to_db(item1,item2):
    connection = openDB()
    csr = connection.cursor()
    try:
        print(item1,item2)
        sql = "INSERT INTO comprehensive (score, level_name) VALUES (%s, %s)"
        val=(item1,item2)
        print("sql = " + str(sql))
        csr.execute(sql,val)
        connection.commit()
        CloseDB()
    except Exception as err:
        print("Failed inserting record:{}".format(err))
    CloseDB()

