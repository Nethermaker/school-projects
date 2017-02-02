import math
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
rw = float(raw_input("What is the width of your rectangle? "))
rh = float(raw_input("What is the height of your rectangle? "))
print "The area of the rectangle is {} and the perimeter is {}.".format(rh*rw, 2*rh + 2*rw)

#Ditto but triangles
tw = float(raw_input("What is the width of your triangle? "))
th = float(raw_input("What is the height of your triangle? "))
print "The area of the triangle is {}.".format((tw*th)/2)

#Average of three numbers
nOne = float(raw_input("Enter the first number: "))
nTwo = float(raw_input("Enter the second number: "))
nThree = float(raw_input("Enter the third number: "))
print "The average of those three numbers is {}.".format((nOne + nTwo + nThree) / 3)

#Area of a trapezoid because I'm unoriginal
bOne = float(raw_input("Enter base 1 of your trapezoid: "))
bTwo = float(raw_input("Enter base 2 of your trapezoid: "))
trapH = float(raw_input("Enter the height of your trapezoid: "))
print "The area of your trapezoid is {}.".format((bOne+bTwo)*0.5*trapH)

#CHALLENGE
a = float(raw_input("Enter an A value: "))
b = float(raw_input("Enter a B value: "))
c = float(raw_input("Enter a C value: "))
print "The roots of this quadratic equation are {} and {}.".format(
    (-b + math.sqrt(b**2 - (4*a*c))) / (2*a),
    (-b - math.sqrt(b**2 - (4*a*c))) / (2*a))
