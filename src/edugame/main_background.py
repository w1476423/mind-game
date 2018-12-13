import arcade


# arcade.open_window(600, 600, "Drawing Example")
# arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

#getting ready to draw
# arcade.start_render()

def draw_snowflake(x,y):

    #90 degree up
    arcade.draw_line(x, y,x, y+50, arcade.color.WHITE, 3)
    arcade.draw_line(x, y+30, x+10, y + 40, arcade.color.WHITE, 3)
    arcade.draw_line(x, y+30, x-10, y + 40, arcade.color.WHITE, 3)

    #0 degree - right
    arcade.draw_line(x, y, x+50, y, arcade.color.WHITE, 3)
    arcade.draw_line(x+30, y, x+40, y + 10, arcade.color.WHITE, 3)
    arcade.draw_line(x+30, y, x+40, y - 10, arcade.color.WHITE, 3)

    #45 degree
    arcade.draw_line(x, y, x+30, y + 30, arcade.color.WHITE, 3)
    arcade.draw_line(x+20, y+20, x+30, y + 20, arcade.color.WHITE, 3)
    arcade.draw_line(x+20, y+20, x+20, y + 30, arcade.color.WHITE, 3)

    #180 degree
    arcade.draw_line(x, y, x-50, y, arcade.color.WHITE, 3)
    arcade.draw_line(x-30, y, x-40, y - 10, arcade.color.WHITE, 3)
    arcade.draw_line(x-30, y, x-40, y + 10, arcade.color.WHITE, 3)

    #270 degree
    arcade.draw_line(x, y,x, y-50, arcade.color.WHITE, 3)
    arcade.draw_line(x, y-30, x-10, y - 40, arcade.color.WHITE, 3)
    arcade.draw_line(x, y-30, x+10, y - 40, arcade.color.WHITE, 3)

    #135 degree
    arcade.draw_line(x, y, x-30, y + 30, arcade.color.WHITE, 3)
    arcade.draw_line(x-20, y+20, x-30, y + 20, arcade.color.WHITE, 3)
    arcade.draw_line(x-20, y+20, x-20, y + 30, arcade.color.WHITE, 3)

    #225 degree
    arcade.draw_line(x, y, x-30, y - 30, arcade.color.WHITE, 3)
    arcade.draw_line(x-20, y-20, x-30, y - 20, arcade.color.WHITE, 3)
    arcade.draw_line(x-20, y-20, x-20, y - 30, arcade.color.WHITE, 3)

    #315 degree
    arcade.draw_line(x, y, x+30, y - 30, arcade.color.WHITE, 3)
    arcade.draw_line(x+20, y-20, x+30, y - 20, arcade.color.WHITE, 3)
    arcade.draw_line(x+20, y-20, x+20, y - 30, arcade.color.WHITE, 3)

# draw_snowflake(200,200)
#finish drawing
# arcade.finish_render()

#keep the window up until someone closes it
# arcade.run()

# def on_draw(delta_time):
#     arcade.start_render()
#     draw_snowflake(150,on_draw.snowflake_move_y)
#     draw_snowflake(250,225)
#     draw_snowflake(450, 300)
#     # on_draw.snowflake_move_y-= 1
#
# on_draw.snowflake_move_y=500
#
# def main():
#     arcade.open_window(900, 600, "Drawing Example")
#     arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
#     draw_snowflake(150,300)
#     arcade.schedule(on_draw,60/60)
#     arcade.run()
#
# main()