width = 17 #int
height = 12.0 #float
period = '.'#string

width / 2 #int
width / 2.0 #float
height / 3 #float
1 + 2 * 5 #int (followed order of operations)
period * 5 #string (printed . 5 times in a row)
#period * period #error

#Rectangle base, height, area, perimeter, etc.

w = float(raw_input("What is the width of your rectangle? "))
h = float(raw_input("What is the height of your rectangle? "))
print "The area of the rectangle is {} and the perimeter is {}.".format(h*w, 2*h + 2*w)

#Ditto but triangles
