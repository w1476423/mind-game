"""
Game 1
"""
import random

from arcade import color, Color

from edugame.api import Game
from edugame.common import *

SHOW_READY = 'show_ready'
GAME_STARTED = 'game_started'
SHOW_NUMBERS = 'show_numbers'
ASK_FOR_NUMBERS = 'ask_for_numbers'
SHOW_SCORE = 'show_score'
EXIT = 'exit'


class SimonNumbers(Game):
    """
    Card-based memory game
    """

    def __init__(self, width: float = 640, height: float = 480, title: str = 'Arcade Window', fullscreen: bool = True,
                 resizable: bool = False):
        super().__init__(width, height, title, fullscreen, resizable)

        self.random_numbers = None
        self.number_color = color.LIGHT_BLUE
        self.buttonStart = GameButton(name="Start", center_x=self.width / 3,
                                      center_y=self.height / 2,
                                      on_click=lambda: self.transition('start'))

        self.set_state(SHOW_READY)

        arcade.set_background_color(color.COOL_GREY)

    def transition(self, action):
        print('action: ' + action)

        if self.state == SHOW_READY:
            if action is 'start':
                self.state = SHOW_NUMBERS

    def game_draw(self):
        super().game_draw()

        if self.state == SHOW_READY:
            self.print_message_center("Press Start When Ready!", color=color.GREEN)

        if self.state == SHOW_NUMBERS:
            self.print_message_center(message=str(self.random_numbers[0]),
                                      color=self.number_color,
                                      size=300)

    elapsed = 0

    def on_update(self, delta_time: float):
        """Movement and game logic"""
        super().on_update(delta_time)

        self.button_list.clear()

        if self.state == SHOW_READY:
            self.button_list.append(self.buttonStart)

        if self.state == SHOW_NUMBERS:
            # generate number list
            if not self.random_numbers:
                self.random_numbers = [random.randint(0, 9)]

        if self.state == ASK_FOR_NUMBERS:
            self.random_numbers = None
            self.print_message_center("Which numbers appeared?", color=color.GREEN)

        if self.state == EXIT:
            self.game_exit()


if __name__ == '__main__':
    x = SimonNumbers()
    x.state = SHOW_READY
    x.on_update(1)
