# Object oriented programming is the idea that you create 'objects' that
#   have certain properties, and when you create a program, you create
#   'instances' of those objects that interact together.

class Pet:

    def __init__(self, name, color, owner, weight):
        
        self.name = name
        self.color = color
        self.owner = owner
        self.weight = weight
        self.x = 0
        self.y = 0


    def eat(self, food):
        print '{} eats the {}. Yum!'.format(self.name, food)
        self.weight += 1

    def move(self, direction):
        if direction in ['north', 'n']:
            self.y += 1
        elif direction in ['east', 'e']:
            self.x += 1
        elif direction in ['south', 's']:
            self.y -= 1
        elif direction in ['west', 'w']:
            self.x -= 1
        else:
            print '{} can\'t travel that way!'.format(self.name)

    def get_location(self):
        return self.x, self.y
            
    


    def __str__(self):

        return 'Hi! My name is {}!'.format(self.name)




class Dog(Pet):

    def __init__(self, name, color, owner, weight, flea_count):

        Pet.__init__(self, name, color, owner, weight)
        self.flea_count = flea_count

    def heel(self, current_x, current_y):
        self.x = current_x
        self.y = current_y

    def roll_over(self):
        print '{} rolls over!'.format(self.name)

    def bark(self):
        print 'Woof!'

    def barf(self):
        self.weight -= 10
        print 'Bllaaahsdjahajhdgggggggggg'


































