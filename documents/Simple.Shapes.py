# This program will use turtle to draw 5 different shapes.

import turtle
turtle.pensize(3)
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.circle(40, steps = 3) #triangle shape

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.circle(40, steps = 4) #square shape

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(40, steps = 5) #pentagon shape

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.circle(40, steps = 6) #hexagon shape

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.circle(40) #circle shape

turtle.done()


