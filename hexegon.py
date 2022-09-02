import turtle

turtle.color("black","grey")
turtle.begin_fill()
for i in range(0,6):
    turtle.forward(50)
    turtle.right(60)
turtle.end_fill()

turtle.exitonclick()