class Vending:

    def __init__(self, cookies_count, water_count, chips_count):

        self.cookies = cookies_count
        self.cookies_c = 1.95
        self.water = water_count
        self.water_c = 0.99
        self.chips = chips_count
        self.chips_c = 1.50
        self.pennies = 100
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
                print self.user
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
            if self.user > 0:
                print 'Not enough money in machine for change. Please enter exact change.'
                self.user = temp_user
                tens = 0
                fives = 0
                ones = 0
                quarters = 0
                dimes = 0
                nickels = 0
                pennies = 0
                while self.user > 0:
                    if self.user >= 10.0:
                        tens += 1
                        self.tens -= 1
                        self.user -= 10.0
                    elif self.user >= 5.0:
                        fives += 1
                        self.fives -= 1
                        self.user -= 5.0
                    elif self.user >= 1.0:
                        ones += 1
                        self.ones -= 1
                        self.user -= 1.0
                    elif self.user >= 0.25:
                        quarters += 1
                        self.quarters -= 1
                        self.user -= 0.25
                    elif self.user >= 0.1:
                        dimes += 1
                        self.dimes -= 1
                        self.user -= 0.1
                    elif self.user >= 0.05:
                        nickels += 1
                        self.nickels -= 1
                        self.user -= 0.05
                    elif self.user >= 0.01:
                        pennies += 1
                        self.pennies -= 1
                        self.user -= 0.01
                return 'You have gotten your money back.'
            else:
                print 'Enjoy your snack!'
                return '''Your change is:
Tens: {}
Fives: {}
Ones: {}
Quarters: {}
Dimes: {}
Nickels: {}
Pennies: {}.'''.format(tens, fives, ones, quarters, dimes, nickels, pennies)
                
    
        
















vending = Vending(15, 10, 20)
