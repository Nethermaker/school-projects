# The following program is supposed to ask a user how much the meal
# cost, how many people ate, and what percentage they are tipping, and
# should return the amount each person should pay.
# Unfortunately, there are several errors in the program. Can you find
# them all?  Here is what the program should look like if it works.
#
# >>> How much was your meal (in dollars)? 82.50
# What percent tip are you leaving? 20
# How many people are contributing to the tip? 4
# You should each leave $______

meal_cost = raw_input ("How much was your meal (in dollars)? ")
percent = raw_input("What percent tip are you leaving? ")
people = raw_input("How many people are contributing to the tip? ")

total_tip = float(meal_cost) * (1 + float(percent)/100)
tip_per_person = float(total_tip) / float(people)
print "You should each leave $" + str(tip_per_person)
