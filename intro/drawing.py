import turtle

my_screen = turtle.Screen()
bob = turtle.Turtle()

def square(side):
    bob.forward(side)
    bob.right(90)
    bob.forward(side)
    bob.right(90)
    bob.forward(side)
    bob.right(90)
    bob.forward(side)
    bob.right(90)

def octagon(side):
    bob.forward(side)
    bob.right(45)
    bob.forward(side)
    bob.right(45)
    bob.forward(side)
    bob.right(45)
    bob.forward(side)
    bob.right(45)
    bob.forward(side)
    bob.right(45)
    bob.forward(side)
    bob.right(45)
    bob.forward(side)
    bob.right(45)
    bob.forward(side)
    bob.right(45)

bob.color('red')
bob.pensize(200)
bob.circle(100)

#octagon(100)

#square(100)

#bob.penup()
#bob.forward(150)
#bob.pendown()

#square(100)





#The bottom
my_screen.exitonclick()
