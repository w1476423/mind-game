"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""

import arcade

# Set up the constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

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


from api import Game


class MainWindow(Game):
    """ Main application class. """

    exited = False

    def __init__(self, width, height):
        super().__init__(width, height, title="Main Window", fullscreen=False, resizable=True)
        self.cursor = None
        self.left_down = False

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

    def update(self, dt):
        """ Move everything """
        if self.left_down:
            self.cursor.angle += 2

    def on_draw(self):
        super().on_draw()
        self.cursor.draw()
        arcade.draw_text('Welcome!', 0, arcade.get_window().height - 30, arcade.color.WHITE, 30)

        if (self.current_state is 'EXITING'):
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text('Thanks for Playing!', 0, arcade.get_window().height / 2,
                             arcade.color.BLUE, 30)
            self.exited = True

    def on_update(self, delta_time: float):
        if self.exited:
            arcade.pause(2)
            exit(0)

    def game_exit(self):
        super().game_exit()
        self.current_state = 'EXITING'
        # exit(0)

    def game_draw(self):
        super().game_draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.cursor.x = x
        self.cursor.y = y


def main():
    window = MainWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    window.set_caption("Educational Game")
    arcade.run()


if __name__ == "__main__":
    main()
