import datetime
import sqlite3

from edugame.api import GameSession

"""
Data access component for games
"""


class DataAccess:

    CREATE_TABLE_STATEMENT = \
        '''create table if not exists game_history 
                                     (ID                INTEGER  PRIMARY KEY, 
                                      USER_ID           INTEGER,   
                                      DATE_PLAYED       DATE     NOT NULL, 
                                      TOTAL_TIME_PLAYED REAL     NOT NULL, 
                                      SCORE             REAL     NOT NULL,
                                      GAME STATISTICS   REAL     NOT NULL)'''

    INSERT_STATEMENT = \
        '''insert into game_history (USER_ID, DATE_PLAYED, TOTAL_TIME_PLAYED, SCORE) values (?,?,?,?)'''

    def __init__(self) -> None:
        super().__init__()
        self.connection = sqlite3.connect(database="statistics.db")
        self.setup()

    def setup(self):
        # create tables
        c = self.connection.cursor()
        c.execute(self.CREATE_TABLE_STATEMENT)

        pass

    def save_game_session(self, game_session:GameSession):
        # TODO: validate
        c = self.connection.cursor()

        c.execute(self.INSERT_STATEMENT, (game_session.user_id,
                                          datetime.date.today(),
                                          game_session.time_played,
                                          game_session.score))

        self.connection.commit()


if __name__ == '__main__':
    data_access = DataAccess()
    print(data_access)

    data_access.save_game_session(GameSession(1, 200, 20))

    connection = sqlite3.connect(database="../statistics.db")
    c = connection.cursor()
    c.execute('''SELECT score FROM game_history''')
    row = c.fetchone()
    print(row[0])
