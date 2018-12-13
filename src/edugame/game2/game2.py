"""
Game 2
"""
import string

from arcade import color

import edugame
from edugame.game1.game1 import Memento, arcade, SHOW_READY


class MementoSymbols(Memento):
    """
    Memory game based on repeating actions
    """
    game_id = '2'

    def __init__(self, width: float = 640, height: float = 480, title: str = 'Arcade Window', resizable: bool = False):
        super().__init__(width, height, title, resizable, list(string.ascii_uppercase))

