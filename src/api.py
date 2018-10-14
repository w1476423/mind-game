"""
API includes interfaces for each game to implement

NOTE: These are not finalized.
"""

from arcade import Window

from common import *


class ExitButton(TextButton):
    def __init__(self, center_x, center_y, exit_handler):
        super().__init__(center_x,
                         center_y,
                         width=50,
                         height=30,
                         text="Exit")
        self.exit_handler = exit_handler

    def on_release(self):
        super().on_release()
        self.exit_handler()



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




class Game(Window):
    """
    Abstract class representing an educational game.
    Games are managed by the Main class, which ensures that certain functionality (e.g. exit) returns control
    back to the main menu.  (not yet implemented)
    """

    current_state = None # TODO: Implement state-based game play

    button_list = []

    def __init__(self, width: float = 800, height: float = 600, title: str = 'Arcade Window', fullscreen: bool = True,
                 resizable: bool = False):
        super().__init__(width, height, title, fullscreen, resizable)

        self.quit_button = ExitButton(width - 50, height - 30, self.game_exit)
        self.button_list = []
        self.button_list.append(self.quit_button)

    def on_draw(self):
        super().on_draw()

        arcade.start_render()

        # Call implementation of draw. This ensures buttons render on top
        self.game_draw()

        for button in self.button_list:
            button.draw()

    def game_draw(self):
        """
        Subclasses should implement this instead of overriding on_draw() to ensure that main window components
        are displayed on top.
        :return:
        """
        pass

    def game_stop(self):
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
        self.game_stop()
        self.game_log_statistics()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        super().on_mouse_press(x, y, button, modifiers)

        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        super().on_mouse_release(x, y, button, modifiers)

        check_mouse_release_for_buttons(x, y, self.button_list)

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
    pass
