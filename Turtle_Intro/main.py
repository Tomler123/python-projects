import turtle as t
import random

### intro ###

def Intro():
    timmy_the_turtle = t.Turtle()
    timmy_the_turtle.shape("turtle")
    timmy_the_turtle.color("red")
    timmy_the_turtle.forward(100)
    timmy_the_turtle.backward(200)
    timmy_the_turtle.right(90)
    timmy_the_turtle.left(180)
    timmy_the_turtle.setheading(0)

# Intro()

### Square ###

def Square():
    square = t.Turtle()
    square.shape("turtle")
    square.color("blue")
    square.forward(100)
    square.left(90)
    square.forward(100)
    square.left(90)
    square.forward(200)
    square.left(90)
    square.forward(200)
    square.left(90)
    square.forward(200)
    square.left(90)
    square.forward(100)
    square.setheading(0)

# Square()

### Draw Dashed Line ###

def DashedLine():
    tim = t.Turtle()

    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

# DashedLine()

### Draw Shapes ###
def Shapes():
    tim = t.Turtle()
    # tim.speed("fastest")
    colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

    def draw_shape(num_sides):
        angle = 360 / num_sides
        for _ in range(num_sides):
            tim.forward(100)
            tim.right(angle)

    for shape_side_n in range(3,10):
        tim.color(random.choice(colors))
        draw_shape(shape_side_n)

# Shapes()

### Random Walk ###

def RandomWalk():
    tim = t.Turtle()
    colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    directions = [0, 90, 180, 270]
    tim.pensize(15)
    tim.speed("fastest")

    for _ in range(200):
        tim.color(random.choice(colors))
        tim.forward(30)
        tim.setheading(random.choice(directions))

# RandomWalk()

### Spirograph ###

def Spirograph():
    tim = t.Turtle()
    t.colormode(255)
    # tim.speed("fastest")

    def random_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        return color

    def draw_spirograph(size_of_gap):
        for _ in range(int(360 / size_of_gap)):
            tim.color(random_color())
            tim.circle(100)
            tim.setheading(tim.heading() + size_of_gap)

    draw_spirograph(5)

# Spirograph()

### Hirst Painting ###

def hirstpainting():
    t.colormode(255)
    tim = t.Turtle()
    tim.speed("fastest")
    tim.penup()
    tim.hideturtle()
    color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
                  (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
                  (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),
                  (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
                  (107, 127, 153), (174, 94, 97), (176, 192, 209)]
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    number_of_dots = 100

    for dot_count in range(1, number_of_dots + 1):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

    screen = t.Screen()
    screen.exitonclick()

hirstpainting()