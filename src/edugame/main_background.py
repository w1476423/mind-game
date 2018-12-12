import arcade

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
