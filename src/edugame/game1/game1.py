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


class Memento(Game):
    """
    Card-based memory game
    """
    game_id = '1'
    total_score = 0
    elapsed = 0
    glyphs = []
    # glyphs = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G' ]
    numbers = []
    game_over = False
    current_level = -1

    def __init__(self, width: float = 640, height: float = 480, title: str = 'Arcade Window',
                 resizable: bool = False, glyphs=None):
        super().__init__(width, height, title, resizable)

        self.number_colors = [color.GREEN, color.YELLOW, color.BLUE, color.WHITE, color.RED, color.ORANGE]

        if not glyphs:
            self.glyphs = [x for x in range(0, 10)]
        else:
            self.glyphs = random.sample(glyphs, 10)

        self.numbers_presented = []
        self.numbers_entered = []
        self.number_correct = 0
        self.seconds_per_number = 1

        # random.shuffle(self.number_colors)

        self.transition(SHOW_READY)

        # start game session

        # load historical statistics

        arcade.set_background_color(color.COOL_GREY)

    def selected_number(self, n):

        current_digit = len(self.numbers_entered)

        if current_digit >= len(self.numbers):
            return

        self.numbers_entered.append(n)

        color = arcade.color.GREEN if n == self.numbers[current_digit] else arcade.color.RED

        label = Label(x = self.width/2 - self.number_count*5 + len(self.label_list)*14,
                                     y = self.height * 1/3,
                                     message=n,
                                     color=color)

        self.label_list.append(label)

        # numStr = ''.join(str(x) for x in self.numbers_entered)
        if len(self.numbers_entered) == self.number_count:
            self.elapsed = 0


    def selected_level(self, i):
        self.current_level = i
        self.number_count = self.current_level*2
        self.transition(SHOW_NUMBERS)

    def get_color(self, i):
        return self.number_colors[i % len(self.number_colors)]

    def transition(self, next_state):
        """Represents actions that occur on transitions between states"""

        self.button_list.clear()
        self.label_list.clear()

        print("(" + str(self.state) + "," + str(next_state) + ")")  # Debug

        if (self.state, next_state) == (GameState.READY, SHOW_READY):

            # buttonStart = GameButton(name="Start", center_x=self.width / 2,
            #                          center_y=self.height / 2 - 50,
            #                          on_click=lambda: self.transition(SHOW_NUMBERS))

            number_buttons = []
            for i in range(1, 8):
                number_buttons.append(
                    GameButton(
                        name=str(i),
                        center_x=self.width / 2 - 10*10 + 30 * (i - 1),
                        center_y=self.height / 2 - 40,
                        on_click=lambda idx=i: self.selected_level(idx))
                )

            self.button_list += number_buttons

            level_label = Label(self.width / 2 - 70, self.height / 2, "Select a Level")

            self.label_list += [level_label]

        if (self.state, next_state) == (SHOW_SCORE, SHOW_NUMBERS):
            # if self.number_correct == self.number_count:
            #     self.number_count += 1
            # else:
            #     self.number_count = max(2, self.number_count - 1)

            # self.number_count = self.current_level  # TODO: populate this from a game level property
            self.number_correct = 0

        if (self.state, next_state) == (SHOW_SCORE, SHOW_NUMBERS) or \
                (self.state, next_state) == (SHOW_READY, SHOW_NUMBERS):
            self.elapsed = 0
            # self.numbers = [ self.glyphs[random.randint(0, 9)] for _ in range(self.number_count)]

            self.numbers = [ random.choice(self.glyphs) for _ in range(self.number_count) ]

            for number in self.numbers:
                label = Label(x=self.width / 2 - self.number_count * 20 + len(self.label_list) * 40,
                              y=self.height * 1 / 2,
                              message=str(number),
                              size=40,
                              color=arcade.color.GREEN)

                label.seed = random.random()
                self.label_list.append(label)

        if (self.state, next_state) == (SHOW_NUMBERS, ASK_FOR_NUMBERS):

            self.button_list = []

            glyph_buttons = []
            for i in range(len(self.glyphs)):
                glyph_buttons.append(
                    GameButton(
                        name=str(self.glyphs[i]),
                        center_x=self.width / 2 - 140 + 30 * i,
                        center_y=self.height / 2 - 40,
                        on_click=lambda idx=self.glyphs[i]: self.selected_number(idx))
                )

            self.button_list += glyph_buttons

        if (self.state, next_state) == (ASK_FOR_NUMBERS, SHOW_SCORE):

            self.number_correct = 0

            # calculate score
            for i in range(self.number_count):
                if self.numbers[i] == self.numbers_entered[i]:
                    self.number_correct += 1

            if self.number_correct != len(self.numbers):
                # missed one
                self.game_over = True

            self.total_score += self.number_correct

            # self.current_level = self.number_count - 1

            # write total_score & current_level to db
            # write_to_db(self.total_score,self.current_level)

        self.state = next_state

    def game_draw(self):
        super().game_draw()

        # if self.state == SHOW_READY:
        #     self.print_message_center("Press Start When Ready!", color=color.GREEN)

        if self.state == SHOW_NUMBERS:
            # total_time = self.seconds_per_number * self.number_count  # 2 seconds per number

            for label in self.label_list:
                label.x += 0.5*random.randint(-1,1)
                label.y += 0.5*random.randint(-1,1)
                label.draw()

        if self.state == SHOW_SCORE:
            self.print_message_center(
                "Score: " + str(self.number_correct) + " out of " + str(self.number_count) + " | Total Score: " + str(
                    self.total_score) + " Level: " + str(self.current_level),
                color.GREEN)

        if self.state == ASK_FOR_NUMBERS:
            self.print_message_center("Which symbols appeared (in order)?", color=color.GREEN)

            for label in self.label_list:
                label.draw()

            if len(self.numbers_entered) >= self.number_count:
                if self.elapsed > 1:
                    self.elapsed = 0
                    self.transition(SHOW_SCORE)

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

                self.numbers.clear()
                self.numbers_entered.clear()
                self.button_list.clear()

                if self.game_over:
                    self.transition(EXIT)
                else:
                    self.transition(SHOW_NUMBERS)

        if self.state == EXIT:
            self.quit_button.on_click()
            self.close()

    def game_exit(self):
        super().game_exit()

    def game_stop(self):
        super().game_stop()
        self.close()


    def game_log_statistics(self):

        if self.current_level != -1:
            write_to_db(self.game_id, self.total_score, self.current_level)


if __name__ == '__main__':
    x = Memento()
    x.state = SHOW_READY
    x.on_update(1)
