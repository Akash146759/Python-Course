import turtle

turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()
 
# first triangle for star
board.forward(100) # draw base
 
board.left(120)
board.forward(100)
 
board.left(120)
board.forward(100)

 
board.penup()
board.right(150)
board.forward(50)

turtle.done()