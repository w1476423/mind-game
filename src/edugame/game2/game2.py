"""
Game 2
"""
import random

from arcade import color, Color

from edugame.api import Game, GameState
from edugame.common import *
from edugame.db import *

SHOW_READY = 'show_ready'
GAME_STARTED = 'game_started'
SHOW_NUMBERS = 'show_numbers'
ASK_FOR_NUMBERS = 'ask_for_numbers'
SHOW_SCORE = 'show_score'
EXIT = 'exit'


class SimonSymbols(Game):
    """
    memory game - symbols
    """

    total_score = 0

    def __init__(self, width: float = 640, height: float = 480, title: str = 'Arcade Window',
                 resizable: bool = False):
        super().__init__(width, height, title, resizable)

        self.symbols_count = 2  # TODO: populate this from a game level property

        self.symbol_colors = [color.GREEN, color.YELLOW, color.BLUE, color.WHITE, color.RED, color.ORANGE]

        self.symbols_presented = []
        self.symbols_entered = []
        self.symbols_correct = 0
        self.seconds_per_symbol = 1

        # random.shuffle(self.number_colors)

        self.transition(SHOW_READY)

        # start game session

        # load historical statistics

        arcade.set_background_color(color.BEAU_BLUE)

    def selected_symbol(self, i):
        self.symbols_entered.append(i)
        if len(self.symbols_entered) == self.symbols_count:
            self.elapsed = 0

    def get_color(self, i):
        return self.symbol_colors[i % len(self.symbol_colors)]

    def transition(self, next_state):
        """Represents actions that occur on transitions between states"""

        self.button_list.clear()

        print("(" + str(self.state) + "," + str(next_state) + ")") # Debug

        if (self.state, next_state) == (GameState.READY, SHOW_READY):
            buttonStart = GameButton(name="Start", center_x=self.width / 2,
                                     center_y=self.height / 2 - 50,
                                     on_click=lambda: self.transition(SHOW_NUMBERS))

            self.button_list += [buttonStart]

        if (self.state, next_state) == (SHOW_SCORE, SHOW_NUMBERS) :
            if self.symbols_correct == self.symbols_count:
                self.symbols_count += 1
            else:
                self.symbols_count = max(2, self.symbols_count - 1)

            self.symbols_correct = 0

        if (self.state, next_state) == (SHOW_SCORE, SHOW_NUMBERS)or \
                (self.state, next_state) == (SHOW_READY, SHOW_NUMBERS):
            self.elapsed = 0
            self.symbols_presented = []
            for i in range(self.symbols_count):
                self.symbols_presented.append(random.choice(['!','@','#','$','%','^','&','*','?','{}']))

        if (self.state, next_state) == (SHOW_NUMBERS, ASK_FOR_NUMBERS):

            self.button_list = []

            symbol_buttons=[]
            symbols = ['!','@','#','$','%','^','&','*','?','{}']
            for i in symbols:
                symbol_buttons.append(
                    GameButton(
                        name=str(i),
                        center_x=self.width / 2 - 140 + 30 * symbols.index(i),
                        center_y=self.height / 2 - 40,
                        on_click=lambda idx=i: self.selected_symbol(idx))
                )

            self.button_list += symbol_buttons

        if (self.state, next_state) == (ASK_FOR_NUMBERS, SHOW_SCORE):

            self.symbols_correct = 0

            # calculate score
            for i in range(self.symbols_count):
                if self.symbols_presented[i] == self.symbols_entered[i]:
                    self.symbols_correct += 1

            self.total_score = self.symbols_correct
            self.current_level = self.symbols_count - 1

            write_to_db('2',self.total_score,self.current_level)

        self.state = next_state

    def game_draw(self):
        super().game_draw()

        if self.state == SHOW_READY:
            self.print_message_center("Press Start When Ready!", color=color.GREEN)

        if self.state == SHOW_NUMBERS:

            total_time = self.seconds_per_symbol * self.symbols_count  # 2 seconds per number

            index = int(self.elapsed * self.symbols_count / total_time)

            # print("elapsed: " + str(self.elapsed) + ' pct: ' + str(self.elapsed / total_time) + ' index: ' + str(index))

            if index < self.symbols_count:
                self.print_message_center(message=str(self.symbols_presented[index]),
                                          color=self.get_color(index),
                                          size=300)

        if self.state == SHOW_SCORE:

            self.print_message_center("Score: " + str(self.symbols_correct) + " out of " + str(self.symbols_count) + " | Total Score: " + str(self.total_score) + " Level: " + str(self.current_level),
                                      color.GREEN)

        if self.state == ASK_FOR_NUMBERS:
            self.print_message_center("Which symbols appeared (in order)?", color=color.GREEN)

            arcade.draw_text(
                text=str(self.symbols_entered),
                start_x=self.width / 2,
                start_y=self.height / 2 - 90,
                anchor_x="center",
                anchor_y="center",
                align="center",
                width=200,
                color=color.YELLOW,
                font_size=13,
                bold=True)

            if len(self.symbols_entered) >= self.symbols_count:
                if self.elapsed > 1:
                    self.elapsed = 0
                    self.transition(SHOW_SCORE)

    elapsed = 0

    def on_update(self, delta_time: float):
        """Movement and game logic"""
        super().on_update(delta_time)

        if self.state == SHOW_NUMBERS:
            self.elapsed += delta_time

            # TODO: make configurable
            if self.elapsed > self.seconds_per_symbol * self.symbols_count:
                self.elapsed = 0
                self.transition(ASK_FOR_NUMBERS)

        if self.state == ASK_FOR_NUMBERS:
            # self.random_numbers = None
            self.elapsed += delta_time

        if self.state == SHOW_SCORE:
            self.elapsed += delta_time
            if self.elapsed > 3:
                self.elapsed = 0
                self.symbols_presented = []
                self.symbols_entered = []
                self.button_list = []
                self.transition(SHOW_NUMBERS)

        if self.state == EXIT:
            self.game_exit()


if __name__ == '__main__':
    x = SimonSymbols()
    x.state = SHOW_READY
    x.on_update(1)
