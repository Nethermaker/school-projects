import turtle
my_screen = turtle.Screen()
bob = turtle.Turtle()

#I'm too lazy to start from scratch so this is all the code from the assignment we did
def rectangle(l,w):
    bob.fd(w)
    bob.rt(90)
    bob.fd(l)
    bob.rt(90)
    bob.fd(w)
    bob.rt(90)
    bob.fd(l)
    bob.rt(90)

def eq_triangle(s):
    bob.fd(s)
    bob.rt(120)
    bob.fd(s)
    bob.rt(120)
    bob.fd(s)
    bob.rt(120)

def star(s):
    bob.fd(s)
    bob.rt(144)
    bob.fd(s)
    bob.rt(144)
    bob.fd(s)
    bob.rt(144)
    bob.fd(s)
    bob.rt(144)
    bob.fd(s)
    bob.rt(144)

def house(size):
    rectangle(size,size)
    bob.lt(60)
    eq_triangle(size)
    bob.rt(60+90)
    bob.fd(size)
    bob.lt(90)
    bob.fd(size*0.4)
    bob.lt(90)
    bob.fd(size*0.4)
    bob.rt(90)
    bob.fd(size*0.2)
    bob.rt(90)
    bob.fd(size*0.4)
    bob.lt(90)
    bob.fd(size*0.4)
    bob.lt(90)
    bob.fd(size*0.6)
    bob.lt(90)
    bob.pu()
    bob.fd(size*0.2)
    bob.pd()
    rectangle(size*0.2,size*0.2)
    bob.pu()
    bob.fd(size*0.4)
    bob.pd()
    rectangle(size*0.2,size*0.2)

#New stuff begins here

turtle.colormode(255)

def ground():
    bob.fd(1000)
    bob.bk(2000)
    bob.home()
    bob.rt(90)
    bob.pu()
    bob.fd(200)
    bob.pencolor(0,255,0)
    bob.pensize(399)
    bob.lt(90)
    bob.pd()
    bob.fd(500)
    bob.bk(1000)
    bob.pencolor(0,0,0)
    bob.pensize(1)
    bob.pu()
    bob.home()
    bob.pd()


ground()
bob.lt(90)
bob.pu()
bob.fd(100)
bob.pd()
bob.rt(90)
house(100)
bob.pu()
bob.home()
bob.rt(180)
bob.fd(200)
bob.rt(90)
bob.pu()
bob.fd(50)
bob.pd()
bob.rt(90)
house(50)
bob.pu()
bob.home()
bob.fd(250)
bob.lt(90)
bob.fd(250)
bob.pd()
bob.color('yellow')
bob.pensize(100)
bob.fd(1)
bob.pensize(10)
bob.seth(0)
bob.fd(150)
bob.bk(150)
bob.seth(45)
bob.fd(150)
bob.bk(150)
bob.seth(90)
bob.fd(150)
bob.bk(150)
bob.seth(135)
bob.fd(150)
bob.bk(150)
bob.seth(180)
bob.fd(150)
bob.bk(150)
bob.seth(225)
bob.fd(150)
bob.bk(150)
bob.seth(270)
bob.fd(150)
bob.bk(150)
bob.seth(315)
bob.fd(150)
bob.bk(150)
bob.seth(0)
bob.pensize(0)
bob.color(0,0,0)
bob.pu()
bob.home()
bob.rt(180)
bob.fd(250)
bob.rt(90)
bob.fd(250)
bob.pd()
bob.write('blue sky')















#The end
my_screen.exitonclick()
