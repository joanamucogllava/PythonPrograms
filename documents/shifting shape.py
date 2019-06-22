import turtle

tim=turtle.Turtle()
turtle.colormode(255)
turtle.speed(0)

for i in range(900):
    turtle.circle(5* i)
    turtle.circle(-5 * i)
    turtle.left(i)
    turtle.color(i,3*i,5*i)
