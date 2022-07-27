from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def main():
    scene_width = 800
    scene_height = 500

    canvas = start_drawing("Beach Scene", scene_width, scene_height)

    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_clouds(canvas, scene_width, scene_height)
    draw_shells(canvas, scene_width, scene_height)
    draw_towel(canvas, scene_width, scene_height)

    finish_drawing(canvas)

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="lightBlue3")

    diameter = 80
    space = 5
    interval = diameter + space

    # Draw sun
    x = 100
    y = 300
    for i in range(1):
        number = random.randint(5, 5)
        if number > 1:
            draw_oval(canvas, x, y,
                    x + diameter, y + diameter, outline="gold1", fill="gold1")
        x += interval


def draw_clouds(canvas, scene_width, scene_height):
    """Draw the clouds. """

    half_height = round(scene_height / 2)
    min_diam = 20
    max_diam = 100

    # Draw 30 circles, each with
    # a random location and diameter.
    for i in range(30):
        x = random.randint(250, scene_width - max_diam)
        y = random.randint(250, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                outline="floralWhite", fill="floralWhite")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 200,
        scene_width, scene_height / 3, width=0, fill="deepSkyBlue4")
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="navajoWhite2")
    
    diameter = 65
    space = 5
    interval = diameter + space
    # Draw Beach Ball
    x = 700
    y = 100
    for i in range(1):
        number = random.randint(5, 5)
        if number > 1:
            draw_oval(canvas, x, y,
                    x + diameter, y + diameter, outline="pink2", fill="hotPink")
        x += interval

def draw_shells(canvas, scene_width, scene_height):
    """Draw shells on the beach. """

    half_height = round(scene_height / 3.8)
    min_diam = 1
    max_diam = 5

    # Draw 100 circles, each with
    # a random location and diameter.
    for i in range(100):
        x = random.randint(5, scene_width - max_diam)
        y = random.randint(5, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                outline="burlywood4", fill="burlywood3")
    
    half_height = round(scene_height / 3.8)
    min_diam = 1
    max_diam = 5

    # Draw 80 circles, each with
    # a random location and diameter.
    for i in range(80):
        x = random.randint(5, scene_width - max_diam)
        y = random.randint(5, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                outline="seashell2", fill="seashell")
    
    half_height = round(scene_height / 3.8)
    min_diam = 1
    max_diam = 5

    # Draw 50 circles, each with
    # a random location and diameter.
    for i in range(50):
        x = random.randint(5, scene_width - max_diam)
        y = random.randint(5, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                outline="mistyRose2", fill="mistyRose1")


def draw_towel(canvas, scene_width, scene_height):
    diameter = 130
    space = 50
    interval = diameter + space
    # Draw towel
    x = 10
    y = 20
    for i in range(1):
        number = random.randint(5, 5)
        if number > 1:
            draw_rectangle(canvas, x, y,
                    x + diameter, y + diameter, outline="firebrick1", fill="mediumSeaGreen")
        x += interval
   
main()