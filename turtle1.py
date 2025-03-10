import turtle    #importing library
turtle.Screen().bgcolor("light blue")
turtle.Screen().setup(700,500)

polygon = turtle.Turtle() #defined variable
 
num_sides = int(input('enter number of sides: '))
side_length = 70
angle = 360.0 / num_sides
#iterate loop for total number of side
for i in range(num_sides):
    polygon.color('red')
    polygon.forward(side_length)
    polygon.left(angle)
 
turtle.done()