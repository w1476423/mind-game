import datetime
import sqlite3
import time


from edugame.api import GameSession

#Create Connection
def create_connection(database ="../statistics.db"):

    try:
        conn = sqlite3.connect("../statistics.db")
        return conn
    except Error as e:
        print (e)

    return None

#Create Tables
def create_table(conn,create_table_sql):

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "../statistics.db"

    #Create User Profile Table
    user_profile_table = """CREATE TABLE IF NOT EXISTS User_Profile(
                                                id_login INTEGER PRIMARY KEY,
                                                name text NOT NULL,
                                                age INTEGER,
                                                creation_date text
                                                );"""
    #Create Game Session Table
    game_session_table = """CREATE TABLE IF NOT EXISTS Game_Session(
                                                id INTEGER PRIMARY KEY,
                                                date_played text,
                                                total_time_played INTEGER,
                                                score INTEGER,
                                                FOREIGN KEY (User_Profile_id) REFERENCES User_info (id_login)
                                                );"""

    #Create Game Levels
    game_levels_table = """CREATE TABLE IF NOT EXISTS Game_Levels(
                                                game_id INTEGER PRIMARY KEY,
                                                levels INTEGER,
                                                total_time_played INTEGER,
                                                score INTEGER,
                                                FOREIGN KEY (user_id) REFERENCES User_info (user_id)
                                                );"""

  #Create Game Statistics
  game_statistics_table = """CREATE TABLE IF NOT EXISTS Game_Statistics(
                                                user_id INTEGER PRIMARY KEY,
                                                date_played text,
                                                total_time_played INTEGER,
                                                score INTEGER,
                                                FOREIGN KEY (user_id) REFERENCES User_info (user_id)
                                                );"""
# create a database connection
    conn = create_connection(database ="../statistics.db")
    if conn is not None:
        # create user_profile table
        create_table(conn, user_profile_table)
        # create user_profile table
        create_table(conn, game_session_table)
        # create game_levels table
        create_table(conn,game_levels_table)
        # create game_statistics table
        create_table(conn,game_statistics_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
