import turtle

turtle.Screen().bgcolor("Aqua")
t = turtle.Turtle()
 
# first triangle for star
t.forward(100) # draw base
 
t.left(120)
t.forward(100)
 
t.left(120)
t.forward(100)
 
t.penup()
t.right(150)
t.forward(50)
 
# second triangle for star
t.pendown()
t.right(90)
t.forward(100)
 
t.right(120)
t.forward(100)
 
t.right(120)
t.forward(100)
 
turtle.done()