import arcade
# Size of the screen.
width=900
height=700
title="RED BALL"
# Size of the circle.
ball_radius=50
# How strong the gravity is.
gravitational_constant=0.6
# Percent of velocity maintained on a bounce.
bounce=0.9

def draw(_delta_time):
    # Start the render.
    arcade.start_render()
    # Draw the ball.
    arcade.draw_circle_filled(draw.x,draw.y,ball_radius,arcade.color.RED)
    draw.x+=draw.delta_x
    draw.y+=draw.delta_y
    draw.delta_y-=gravitational_constant
    # Figure out if we hit the left or right edge and need to reverse.
    if draw.x<ball_radius and draw.delta_x<0:
        draw.delta_x*=-bounce
    elif draw.x>width-ball_radius and draw.delta_x>0:
        draw.delta_x*=-bounce
    # See if we hit the bottom.
    if draw.y<ball_radius and draw.delta_y<0:
        if draw.delta_y*-1>gravitational_constant*15:
            draw.delta_y*=-bounce
        else:
            draw.delta_y*=-bounce/2

draw.x=ball_radius
draw.y=height
draw.delta_x=3
draw.delta_y=3

def main():
    # Open up our window.
    arcade.open_window(width,height,title)
    arcade.set_background_color(arcade.color.GREEN)
    # Tell the computer to call the draw command at the specified interval.
    arcade.schedule(draw,1/80)
    # Run the program.
    arcade.run()
    # When done running the program, close the window.
    arcade.close_window()
main()