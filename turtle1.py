import turtle    #importing library
turtle.Screen().bgcolor("light blue")
turtle.Screen().setup(300,300)
polygon = turtle.Turtle() #defined variable
 
num_sides = 8 #variable
side_length = 50
angle = 360.0 / num_sides
#iterate loop for total number of side
for i in range(num_sides):
    polygon.backward(side_length)
    polygon.left(angle)
     
turtle.done()