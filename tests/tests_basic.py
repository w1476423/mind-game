import sqlite3

import pytest

from edugame.api import GameSession
from edugame.db import DataAccess


@pytest.fixture
def db_connection():

    def _get_connection(name):
        return sqlite3.connect(database=name)

    return _get_connection

def test_db_save_game_session(db_connection):

    connection = db_connection("./statistics.db")

    data_access = DataAccess()

    assert data_access is not None

    data_access.save_game_session(GameSession(1, 200, 20))

    c = connection.cursor()
    c.execute('''SELECT score FROM game_history''')
    row = c.fetchone()

    assert row[0] == 20.0
