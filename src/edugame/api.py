"""
API includes interfaces for each game to implement

NOTE: These are not finalized.
"""
import arcade
from arcade import Window

import datetime

from edugame import common
from edugame.common import TextButton, GameButton
from main_background import draw_snowflake


# icenter_x=width - 25, center_y=height - 15, width=50, height=30, text="Exit", font_size=20)

def check_mouse_press_for_buttons(x, y, button_list):
    """ Given an x, y, see if we need to register any button clicks. """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()


def check_mouse_release_for_buttons(x, y, button_list):
    """ Given an x, y, see if we need to register any button clicks. """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_release()


from enum import Enum


class GameState(Enum):
    READY = 'Ready'
    EXITING = 'Exiting'
    CLOSING = 'Closing'
    STARTING = 'Starting'
    STOPPED = 'Stopped'

class Game(Window):
    """
    Abstract class representing an educational game.
    Games are managed by the Main class, which ensures that certain functionality (e.g. exit) returns control
    back to the main menu.  (not yet implemented)
    """

    current_state = None  # TODO: Implement state-based game play

    button_list = []
    label_list = []

    def __init__(self, width: float = 800, height: float = 600, title: str = 'Arcade Window', fullscreen: bool = False,
                 resizable: bool = False, game_exit = None):
        super().__init__(width, height, title, fullscreen, resizable)

        self.quit_button = GameButton(self.width - 50, self.height - 30, "Exit", self.game_exit)

        self.button_list = []
        self.label_list = []

        self.state = GameState.READY

    def on_draw(self):
        super().on_draw()

        arcade.start_render()

        # Call implementation of draw. This ensures buttons render on top
        self.game_draw()

        for label in self.label_list:
            label.draw()

        for button in self.button_list:
            button.draw()

        self.quit_button.draw()

    def game_play(self):
        """"
        Subclasses should implement this instead of overriding on_update() """

    def game_draw(self):
        """
        Subclasses should implement this instead of overriding on_draw() to ensure that main window components
        are displayed on top.

        call your drawing functions here
        :return:
        """

        # draw_snowflake(200,300)



    def game_stop(self):
        print('game_stop')
        pass

    def game_start(self):
        pass

    def print_help(self):
        pass

    def game_log_statistics(self):
        # TODO: log game statistics to disk for the player
        print("TODO: Write game statistics...")
        pass

    def game_exit(self):
        """
        Show exit screen and return to the main menu
        :return:
        """
        print('Exiting')
        self.set_state(GameState.EXITING)
        self.game_stop()
        self.game_log_statistics()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        super().on_mouse_press(x, y, button, modifiers)

        check_mouse_press_for_buttons(x, y, self.button_list)
        check_mouse_press_for_buttons(x, y, [self.quit_button])

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        super().on_mouse_release(x, y, button, modifiers)

        check_mouse_release_for_buttons(x, y, self.button_list)
        check_mouse_release_for_buttons(x, y, [self.quit_button])

    def set_state(self, state):
        self.state = state

    def print_message(self, message, color):
        """Prints a standard message on the center of the screen."""

        xpos = 20
        ypos = self.height

        size = common.FONT_SIZE

        arcade.draw_text(
            text=message,
            start_x=xpos,
            start_y=ypos,
            anchor_x="left",
            anchor_y="top",
            width=size*len(message),
            color=color,
            font_size=size,
            bold=True)

    def print_message_center(self, message, color, size = common.FONT_SIZE):
        """Prints a standard message on the center of the screen."""

        xpos = self.width / 2
        ypos = self.height / 2

        arcade.draw_text(
            text=message,
            start_x=xpos,
            start_y=ypos,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=size*len(message),
            color=color,
            font_size=size,
            bold=True)

    """
    Handle common key presses, like ESC(exit) and F1 (help)
    """

    def on_key_press(self, symbol: int, modifiers: int):
        super().on_key_press(symbol, modifiers)

        if symbol == arcade.key.ESCAPE:
            self.game_exit()
        elif symbol == arcade.key.F1:
            self.print_help()


class GameSession:
    """
    Represents the life cycle of a game from start to finish.
    """

    def __init__(self, user_id, time_played, score) -> None:
        super().__init__()
        self.user_id = user_id
        self.time = datetime.datetime.now()
        self.time_played = time_played
        self.score = score
