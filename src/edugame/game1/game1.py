"""
Game 1
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


class SimonNumbers(Game):
    """
    Card-based memory game
    """

    total_score = 0

    def __init__(self, width: float = 640, height: float = 480, title: str = 'Arcade Window',
                 resizable: bool = False):
        super().__init__(width, height, title, resizable)

        self.number_count = 2  # TODO: populate this from a game level property

        self.number_colors = [color.GREEN, color.YELLOW, color.BLUE, color.WHITE, color.RED, color.ORANGE]

        self.numbers_presented = []
        self.numbers_entered = []
        self.number_correct = 0
        self.seconds_per_number = 1

        # random.shuffle(self.number_colors)

        self.transition(SHOW_READY)

        # start game session

        # load historical statistics

        arcade.set_background_color(color.COOL_GREY)

    def selected_number(self, i):
        self.numbers_entered.append(i)
        if len(self.numbers_entered) == self.number_count:
            self.elapsed = 0

    def get_color(self, i):
        return self.number_colors[i % len(self.number_colors)]

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
            if self.number_correct == self.number_count:
                self.number_count += 1
            else:
                self.number_count = max(2, self.number_count - 1)

            self.number_correct = 0

        if (self.state, next_state) == (SHOW_SCORE, SHOW_NUMBERS)or \
                (self.state, next_state) == (SHOW_READY, SHOW_NUMBERS):
            self.elapsed = 0
            self.numbers_presented = []
            for i in range(self.number_count):
                self.numbers_presented.append(random.randint(0, 9))

        if (self.state, next_state) == (SHOW_NUMBERS, ASK_FOR_NUMBERS):

            self.button_list = []

            number_buttons = []
            for i in range(10):
                number_buttons.append(
                    GameButton(
                        name=str(i),
                        center_x=self.width / 2 - 140 + 30 * i,
                        center_y=self.height / 2 - 40,
                        on_click=lambda idx=i: self.selected_number(idx))
                )

            self.button_list += number_buttons

        if (self.state, next_state) == (ASK_FOR_NUMBERS, SHOW_SCORE):

            self.number_correct = 0

            # calculate score
            for i in range(self.number_count):
                if self.numbers_presented[i] == self.numbers_entered[i]:
                    self.number_correct += 1

            self.total_score = self.number_correct
            self.current_level = self.number_count - 1
            
            # write total_score & current_level to db
            write_to_db(self.total_score,self.current_level)
            
        self.state = next_state

    def game_draw(self):
        super().game_draw()

        if self.state == SHOW_READY:
            self.print_message_center("Press Start When Ready!", color=color.GREEN)

        if self.state == SHOW_NUMBERS:

            total_time = self.seconds_per_number * self.number_count  # 2 seconds per number

            index = int(self.elapsed * self.number_count / total_time)

            # print("elapsed: " + str(self.elapsed) + ' pct: ' + str(self.elapsed / total_time) + ' index: ' + str(index))

            if index < self.number_count:
                self.print_message_center(message=str(self.numbers_presented[index]),
                                          color=self.get_color(index),
                                          size=300)

        if self.state == SHOW_SCORE:

            self.print_message_center("Score: " + str(self.number_correct) + " out of " + str(self.number_count) + " | Total Score: " + str(self.total_score) + " Level: " + str(self.current_level),
                                      color.GREEN)

        if self.state == ASK_FOR_NUMBERS:
            self.print_message_center("Which numbers appeared (in order)?", color=color.GREEN)

            arcade.draw_text(
                text=str(self.numbers_entered),
                start_x=self.width / 2,
                start_y=self.height / 2 - 90,
                anchor_x="center",
                anchor_y="center",
                align="center",
                width=200,
                color=color.YELLOW,
                font_size=13,
                bold=True)

            if len(self.numbers_entered) >= self.number_count:
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
            if self.elapsed > self.seconds_per_number * self.number_count:
                self.elapsed = 0
                self.transition(ASK_FOR_NUMBERS)

        if self.state == ASK_FOR_NUMBERS:
            # self.random_numbers = None
            self.elapsed += delta_time

        if self.state == SHOW_SCORE:
            self.elapsed += delta_time
            if self.elapsed > 3:
                self.elapsed = 0
                self.numbers_presented = []
                self.numbers_entered = []
                self.button_list = []
                self.transition(SHOW_NUMBERS)

        if self.state == EXIT:
            self.game_exit()


if __name__ == '__main__':
    x = SimonNumbers()
    x.state = SHOW_READY
    x.on_update(1)
