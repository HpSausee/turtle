import turtle

turtle.pensize(3)
#turtle.color("black","red")
turtle.pencolor("red")
turtle.fillcolor("black")
turtle.begin_fill()

for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)

turtle.end_fill()
turtle.exitonclick()