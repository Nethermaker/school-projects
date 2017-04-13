import random

class Vending:

    def __init__(self, cookies_count, water_count, chips_count):

        self.cookies = cookies_count
        self.cookies_c = 1.95
        self.water = water_count
        self.water_c = 0.99
        self.chips = chips_count
        self.chips_c = 1.50
        self.pennies = 50
        self.nickels = 20
        self.dimes = 20
        self.quarters = 30
        self.ones = 10
        self.fives = 5
        self.tens = 2
        self.user = 0.0

    def enter_money(self, pennies=0, nickels=0, dimes=0, quarters=0, ones=0, fives=0, tens=0):
        '''Allows the user to enter a specified amount of money'''
        self.pennies += pennies
        self.nickels += nickels
        self.dimes += dimes
        self.quarters += quarters
        self.ones += ones
        self.fives += fives
        self.tens += tens
        self.user += (pennies*0.01) + (nickels*0.05) + (dimes*0.1) + (quarters*0.25) + \
                     (ones*1.0) + (fives*5.0) + (tens*10.0)
        print 'You have entered {} so far.'.format(self.user)

    def machine_total(self):
        print 'The machine contains ${}'.format(self.tens*10.0 + self.fives*5.0 + self.ones*1.0 \
                                                + self.quarters*0.25 + self.dimes*0.1 + \
                                                self.nickels*0.05 + self.pennies*0.01)

    def get_cookies(self):
        '''Purchase some cookies'''
        if self.cookies == 0:
            return 'Sorry, we are sold out of that item.'
        elif self.user < self.cookies_c:
            return 'Those cost $1.95. Please enter more money.'
        elif self.user >= self.cookies_c:
            temp_user = self.user
            self.user -= self.cookies_c
            tens = 0
            fives = 0
            ones = 0
            quarters = 0
            dimes = 0
            nickels = 0
            pennies = 0
            while self.user > 0.0:
                self.user = round(self.user, 2)
                if self.user >= 10.0 and self.tens > 0:
                    tens += 1
                    self.tens -= 1
                    self.user -= 10.0
                elif self.user >= 5.0 and self.fives > 0:
                    fives += 1
                    self.fives -= 1
                    self.user -= 5.0
                elif self.user >= 1.0 and self.ones > 0:
                    ones += 1
                    self.ones -= 1
                    self.user -= 1.0
                elif self.user >= 0.25 and self.quarters > 0:
                    quarters += 1
                    self.quarters -= 1
                    self.user -= 0.25
                elif self.user >= 0.1 and self.dimes > 0:
                    dimes += 1
                    self.dimes -= 1
                    self.user -= 0.1
                elif self.user >= 0.05 and self.nickels > 0:
                    nickels += 1
                    self.nickels -= 1
                    self.user -= 0.05
                elif self.user >= 0.01 and self.pennies > 0:
                    pennies += 1
                    self.pennies -= 1
                    self.user -= 0.01
                else:
                    break
            self.cookies -= 1
            if self.user > 0:
                self.cookies += 1
                print 'Not enough money in machine for change. Please enter exact change.'
                self.user = temp_user
                self.tens += tens
                self.fives += fives
                self.ones += ones
                self.quarters += quarters
                self.dimes += dimes
                self.nickels += nickels
                self.pennies += pennies
                while self.user > 0:
                    self.user = round(self.user, 2)
                    if self.user >= 10.0:
                        self.tens -= 1
                        self.user -= 10.0
                    elif self.user >= 5.0:
                        self.fives -= 1
                        self.user -= 5.0
                    elif self.user >= 1.0:
                        self.ones -= 1
                        self.user -= 1.0
                    elif self.user >= 0.25:
                        self.quarters -= 1
                        self.user -= 0.25
                    elif self.user >= 0.1:
                        self.dimes -= 1
                        self.user -= 0.1
                    elif self.user >= 0.05:
                        self.nickels -= 1
                        self.user -= 0.05
                    elif self.user >= 0.01:
                        self.pennies -= 1
                        self.user -= 0.01
                print 'You have gotten your money back.'
            else:
                print 'Enjoy your snack!'
                print '''Your change is:
Tens: {}
Fives: {}
Ones: {}
Quarters: {}
Dimes: {}
Nickels: {}
Pennies: {}'''.format(tens, fives, ones, quarters, dimes, nickels, pennies)

    def get_chips(self):
        '''Purchase some cookies'''
        if self.chips == 0:
            return 'Sorry, we are sold out of that item.'
        elif self.user < self.chips_c:
            return 'Those cost $1.95. Please enter more money.'
        elif self.user >= self.chips_c:
            temp_user = self.user
            self.user -= self.chips_c
            tens = 0
            fives = 0
            ones = 0
            quarters = 0
            dimes = 0
            nickels = 0
            pennies = 0
            while self.user > 0.0:
                self.user = round(self.user, 2)
                if self.user >= 10.0 and self.tens > 0:
                    tens += 1
                    self.tens -= 1
                    self.user -= 10.0
                elif self.user >= 5.0 and self.fives > 0:
                    fives += 1
                    self.fives -= 1
                    self.user -= 5.0
                elif self.user >= 1.0 and self.ones > 0:
                    ones += 1
                    self.ones -= 1
                    self.user -= 1.0
                elif self.user >= 0.25 and self.quarters > 0:
                    quarters += 1
                    self.quarters -= 1
                    self.user -= 0.25
                elif self.user >= 0.1 and self.dimes > 0:
                    dimes += 1
                    self.dimes -= 1
                    self.user -= 0.1
                elif self.user >= 0.05 and self.nickels > 0:
                    nickels += 1
                    self.nickels -= 1
                    self.user -= 0.05
                elif self.user >= 0.01 and self.pennies > 0:
                    pennies += 1
                    self.pennies -= 1
                    self.user -= 0.01
                else:
                    break
            self.chips -= 1
            if self.user > 0:
                self.chips += 1
                print 'Not enough money in machine for change. Please enter exact change.'
                self.user = temp_user
                self.tens += tens
                self.fives += fives
                self.ones += ones
                self.quarters += quarters
                self.dimes += dimes
                self.nickels += nickels
                self.pennies += pennies
                while self.user > 0:
                    self.user = round(self.user, 2)
                    if self.user >= 10.0:
                        self.tens -= 1
                        self.user -= 10.0
                    elif self.user >= 5.0:
                        self.fives -= 1
                        self.user -= 5.0
                    elif self.user >= 1.0:
                        self.ones -= 1
                        self.user -= 1.0
                    elif self.user >= 0.25:
                        self.quarters -= 1
                        self.user -= 0.25
                    elif self.user >= 0.1:
                        self.dimes -= 1
                        self.user -= 0.1
                    elif self.user >= 0.05:
                        self.nickels -= 1
                        self.user -= 0.05
                    elif self.user >= 0.01:
                        self.pennies -= 1
                        self.user -= 0.01
                print 'You have gotten your money back.'
            else:
                print 'Enjoy your snack!'
                print '''Your change is:
Tens: {}
Fives: {}
Ones: {}
Quarters: {}
Dimes: {}
Nickels: {}
Pennies: {}'''.format(tens, fives, ones, quarters, dimes, nickels, pennies)

    def get_water(self):
        '''Purchase some cookies'''
        if self.water == 0:
            return 'Sorry, we are sold out of that item.'
        elif self.user < self.water_c:
            return 'Those cost $1.95. Please enter more money.'
        elif self.user >= self.water_c:
            temp_user = self.user
            self.user -= self.water_c
            tens = 0
            fives = 0
            ones = 0
            quarters = 0
            dimes = 0
            nickels = 0
            pennies = 0
            while self.user > 0.0:
                self.user = round(self.user, 2)
                if self.user >= 10.0 and self.tens > 0:
                    tens += 1
                    self.tens -= 1
                    self.user -= 10.0
                elif self.user >= 5.0 and self.fives > 0:
                    fives += 1
                    self.fives -= 1
                    self.user -= 5.0
                elif self.user >= 1.0 and self.ones > 0:
                    ones += 1
                    self.ones -= 1
                    self.user -= 1.0
                elif self.user >= 0.25 and self.quarters > 0:
                    quarters += 1
                    self.quarters -= 1
                    self.user -= 0.25
                elif self.user >= 0.1 and self.dimes > 0:
                    dimes += 1
                    self.dimes -= 1
                    self.user -= 0.1
                elif self.user >= 0.05 and self.nickels > 0:
                    nickels += 1
                    self.nickels -= 1
                    self.user -= 0.05
                elif self.user >= 0.01 and self.pennies > 0:
                    pennies += 1
                    self.pennies -= 1
                    self.user -= 0.01
                else:
                    break
            self.water -= 1
            if self.user > 0:
                self.water += 1
                print 'Not enough money in machine for change. Please enter exact change.'
                self.user = temp_user
                self.tens += tens
                self.fives += fives
                self.ones += ones
                self.quarters += quarters
                self.dimes += dimes
                self.nickels += nickels
                self.pennies += pennies
                while self.user > 0:
                    self.user = round(self.user, 2)
                    if self.user >= 10.0:
                        self.tens -= 1
                        self.user -= 10.0
                    elif self.user >= 5.0:
                        self.fives -= 1
                        self.user -= 5.0
                    elif self.user >= 1.0:
                        self.ones -= 1
                        self.user -= 1.0
                    elif self.user >= 0.25:
                        self.quarters -= 1
                        self.user -= 0.25
                    elif self.user >= 0.1:
                        self.dimes -= 1
                        self.user -= 0.1
                    elif self.user >= 0.05:
                        self.nickels -= 1
                        self.user -= 0.05
                    elif self.user >= 0.01:
                        self.pennies -= 1
                        self.user -= 0.01
                print 'You have gotten your money back.'
            else:
                print 'Enjoy your snack!'
                print '''Your change is:
Tens: {}
Fives: {}
Ones: {}
Quarters: {}
Dimes: {}
Nickels: {}
Pennies: {}'''.format(tens, fives, ones, quarters, dimes, nickels, pennies)


    def shake(self):
        print 'You shake the vending machine! Cheater...'
        chance = random.randint(0,3)
        if chance == 0:
            print 'A bag of chips falls to the bottom.'
            self.chips -= 1
        elif chance == 1:
            print 'A package of cookies falls to the bottom.'
            self.cookies -= 1
        elif chance == 2:
            print 'A bottle of water falls to the bottom.'
            self.water -= 1
        elif chance == 3:
            print 'You hear someone come up behind you.'
            print '"Hey! That\'s called stealing, you know!"'
            print 'The police have been called to your location.'
            print 'You will rot in prison for the rest of your life.'
            while True:
                pass
            
        

    def __str__(self):
        print '''This vending machine has:
Cookies: {}
Chips: {}
Waters: {}

CHANGE:
Tens: {}
Fives: {}
Ones: {}
Quarters: {}
Dimes: {}
Nickels: {}
Pennies: {}'''.format(self.cookies, self.chips, self.water, self.tens, self.fives,
                      self.ones, self.quarters, self.dimes, self.nickels, self.pennies)
        return ''


                
    
        
















vending = Vending(15, 10, 20)
print 'Welcome to the vending machine!'
