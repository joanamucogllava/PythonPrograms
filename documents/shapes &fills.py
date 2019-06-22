import turtle
tim = turtle.Turtle()
colors = ['red', 'blue', 'yellow', 'purple']
tim.color('yellow','blue')
tim.width(5)
tim.begin_fill()
for x in range(6):
    tim.pendown()
    tim.circe(50)
    tim.penup()
    tim.right(60)
    tim.forward(100)
tim.end_fill ()
