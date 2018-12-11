import datetime
import sqlite3
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

# from edugame.api import GameSession

# """
# Data access component for games
# """


# class DataAccess:

#     CREATE_TABLE_STATEMENT = \
#         '''create table if not exists game_history 
#                                      (ID                INTEGER  PRIMARY KEY, 
#                                       USER_ID           INTEGER,   
#                                       DATE_PLAYED       DATE     NOT NULL, 
#                                       TOTAL_TIME_PLAYED REAL     NOT NULL, 
#                                       SCORE             REAL     NOT NULL,
#                                       GAME STATISTICS   REAL     NOT NULL)'''

#     INSERT_STATEMENT = \
#         '''insert into game_history (USER_ID, DATE_PLAYED, TOTAL_TIME_PLAYED, SCORE) values (?,?,?,?)'''

#     def __init__(self) -> None:
#         super().__init__()
#         self.connection = sqlite3.connect(database="statistics.db")
#         self.setup()

#     def setup(self):
#         # create tables
#         c = self.connection.cursor()
#         c.execute(self.CREATE_TABLE_STATEMENT)

#         pass

#     def save_game_session(self, game_session:GameSession):
#         # TODO: validate
#         c = self.connection.cursor()

#         c.execute(self.INSERT_STATEMENT, (game_session.user_id,
#                                           datetime.date.today(),
#                                           game_session.time_played,
#                                           game_session.score))

#         self.connection.commit()


# if __name__ == '__main__':
#     data_access = DataAccess()
#     print(data_access)

#     data_access.save_game_session(GameSession(1, 200, 20))

#     connection = sqlite3.connect(database="../statistics.db")
#     c = connection.cursor()
#     c.execute('''SELECT score FROM game_history''')
#     row = c.fetchone()
#     print(row[0])
