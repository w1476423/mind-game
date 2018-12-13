"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""

import arcade
#equivalent of set PYTHONPATH=src
import os, sys
path=os.path.abspath(__file__)
fd=os.path.dirname(path)
directoryName=os.path.dirname(fd)
sys.path.append(directoryName)

# Set up the constants
import edugame
from edugame import common
from edugame.common import GameButton
from edugame.game1.game1 import SimonNumbers


RECT_WIDTH = 50
RECT_HEIGHT = 50


class Cursor:
    """ Class to represent a cursor on the screen """

    def __init__(self, x, y, angle, color):
        """ Initialize our rectangle variables """

        # Position
        self.x = x
        self.y = y

        # Angle
        self.angle = angle

        # Color
        self.color = color

    def draw(self):
        """ Draw our triangle """
        arcade.draw_triangle_outline(self.x, self.y, self.x, self.y - 20, self.x + 15, self.y - 15, self.color,
                                     border_width=2)


from edugame.api import Game, GameState

NUMBER_OF_GAMES = 2

class MainWindow(Game):
    """ Main application class. """

    def __init__(self, width = common.SCREEN_WIDTH, height = common.SCREEN_HEIGHT):
        super().__init__(width, height, title="Main Window", fullscreen=False, resizable=False)

        self.game1_button = GameButton(center_x=self.width / 3,
                                       center_y=self.height * 1 / 2,
                                       name="Numbers",
                                       on_click=self.start_simon)

        self.game2_button = GameButton(center_x=self.width * 2/3,
                                       center_y=self.height * 1 / 2,
                                       name="Symbols",
                                       on_click=self.start_simon)



        self.stats_button = GameButton(center_x=self.width / 2,
                                       center_y=self.height * 1/3,
                                       name="Statistics",
                                       on_click=self.start_simon)
        self.cursor = None
        self.left_down = False
        self.game = None

    def setup(self):
        width, height = self.get_size()
        self.set_viewport(0, width, 0, height)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLUE_GRAY)

        """ Set up the game and initialize the variables. """
        angle = 0
        color = arcade.color.WHITE
        self.cursor = Cursor(0, height, angle, color)
        self.left_down = False

        self.button_list.append(self.game1_button)
        self.button_list.append(self.game2_button)
        self.button_list.append(self.stats_button)

    def update(self, dt):
        """ Move everything """
        if self.left_down:
            self.cursor.angle += 2

    def handle_exit(self):
        if self.game:
            self.game.close()
            self.game = None
            self.set_visible(True)
            self.set_state(GameState.READY)

    def start_simon(self):
        if not self.game:
            self.game = SimonNumbers()
            self.game.quit_button.on_click = self.handle_exit
            arcade.set_window(self.game)
            self.game.game_start()
            self.set_visible(False)


    def on_draw(self):
        super().on_draw()

        if not self.game:
            self.cursor.draw()

        if self.state is GameState.READY:
            self.print_message('Welcome! Select a Game:', color=arcade.color.GREEN)

        if self.state is GameState.CLOSING:
            self.button_list.clear()
            arcade.set_background_color(arcade.color.BLUE)
            self.print_message_center("Thanks for playing!", color=arcade.color.WHITE)

    close_timer = 0

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        super().on_mouse_press(x, y, button, modifiers)

        if button == arcade.MOUSE_BUTTON_LEFT:
            self.left_down = True

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        super().on_mouse_release(x, y, button, modifiers)

        self.left_down = False

    def on_update(self, delta_time: float):

        super().on_update(delta_time)

        if self.state is GameState.EXITING:
            self.set_state(GameState.CLOSING)

        elif self.state is GameState.CLOSING:
            self.close_timer += delta_time
            if self.close_timer >= 2.0:
                self.close()

    def game_exit(self):
        super().game_exit()

    def game_draw(self):
        super().game_draw()
        
        # for pos in self.snowflake_positions:
        #     draw_snowflake(pos["x"], pos["y"])

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.cursor.x = x
        self.cursor.y = y


def main():
    window = MainWindow()
    window.setup()
    window.set_caption("M!ndGames")
    arcade.run()
    arcade.close_window()


if __name__ == "__main__":
    main()
