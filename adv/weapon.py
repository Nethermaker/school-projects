import random

class Enemy:

    def __init__(self, hp):

        self.hp = hp



class Weapon:

    def __init__(self, name, damage, durability, weight, cost, accuracy):

        self.name = name
        self.damage = damage
        self.max_durability = durability
        self.durability = durability
        self.weight = weight
        self.cost = cost
        self.accuracy = accuracy


    def attack(self, enemy):

        hit_chance = random.randint(1,100)
        if hit_chance <= self.accuracy:
            enemy.hp -= self.damage
            self.durability -= 1
        else:
            print 'You missed!'

    def repair(self):
        self.durability = self.max_durability

    def __str__(self):
        return '''Name: {}
Damage: {}
Durability: {}
Weight: {}
Cost: {}
Accuracy: {}'''.format(self.name, self.damage, self.durability, self.weight, self.cost, self.accuracy)
    
        
class MasterSword(Weapon):

    def __init__(self, name, damage, weight, cost, accuracy):

        Weapon.__init__(self, name, damage, 'Infinite', weight, cost, accuracy)

    def attack(self, enemy):

        hit_chance = random.randint(1,100)
        if hit_chance <= self.accuracy:
            enemy.hp -= self.damage
        else:
            print 'You missed!'
