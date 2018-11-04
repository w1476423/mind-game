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

    def __init__(self, width: float = 640, height: float = 480, title: str = 'Arcade Window',
                 resizable: bool = False):
        super().__init__(width, height, title, resizable)

        self.random_numbers = None
        self.number_count = 2  # TODO: populate this from a game level property

        self.number_colors = [color.GREEN, color.YELLOW, color.BLUE, color.WHITE, color.RED, color.ORANGE]
        # random.shuffle(self.number_colors)

        self.buttonStart = GameButton(name="Start", center_x=self.width / 3,
                                      center_y=self.height / 2,
                                      on_click=lambda: self.transition(SHOW_NUMBERS))

        self.number_buttons = []
        for i in range(10):
            self.number_buttons.append(
                GameButton(
                    name=str(i),
                    center_x=self.width / 2 - 140 + 30 * i,
                    center_y=self.height / 2 - 40,
                    on_click=lambda idx=i: self.selected_number(idx))
            )

        self.transition(SHOW_READY)

        arcade.set_background_color(color.COOL_GREY)

    def selected_number(self, i):
        print("Selected: " + str(i))

    def get_color(self, i):
        return self.number_colors[i % len(self.number_colors)]

    def transition(self, next_state):

        self.button_list.clear()

        if next_state == SHOW_READY:
            self.button_list += [self.buttonStart]

        if next_state == ASK_FOR_NUMBERS:
            self.button_list += self.number_buttons

        self.state = next_state

    def game_draw(self):
        super().game_draw()

        if self.state == SHOW_READY:
            self.print_message_center("Press Start When Ready!", color=color.GREEN)

        if self.state == SHOW_NUMBERS:

            total_time = 2 * len(self.random_numbers)  # 2 seconds per number

            index = int(self.elapsed * self.number_count / total_time)

            # print("elapsed: " + str(self.elapsed) + ' pct: ' + str(self.elapsed / total_time) + ' index: ' + str(index))

            if index < len(self.random_numbers):
                self.print_message_center(message=str(self.random_numbers[index]),
                                          color=self.get_color(index),
                                          size=300)

        if self.state == ASK_FOR_NUMBERS:
            self.print_message_center("Which numbers appeared?", color=color.GREEN)

    elapsed = 0

    def on_update(self, delta_time: float):
        """Movement and game logic"""
        super().on_update(delta_time)

        if self.state == SHOW_NUMBERS:
            # generate number list
            if not self.random_numbers:
                self.random_numbers = []
                self.elapsed = 0
                for i in range(self.number_count):
                    self.random_numbers.append(random.randint(0, 9))

            self.elapsed += delta_time

            # TODO: make configurable
            if self.elapsed > 2 * self.number_count:
                self.transition(ASK_FOR_NUMBERS)

        if self.state == ASK_FOR_NUMBERS:
            self.random_numbers = None
            self.elapsed = 0

        if self.state == EXIT:
            self.game_exit()


if __name__ == '__main__':
    x = SimonNumbers()
    x.state = SHOW_READY
    x.on_update(1)
