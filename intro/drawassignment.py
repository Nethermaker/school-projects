import turtle
my_screen = turtle.Screen()
bob = turtle.Turtle()

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


#rectangle(100,200)
#eq_triangle(200)
#star(300)
#house(200)



















#The end
my_screen.exitonclick()
