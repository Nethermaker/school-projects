class Rock:

    def __init__(self, rock_type, texture, color, weight, size):

        self.type = rock_type
        self.texture = texture
        self.color = color
        self.weight = weight
        self.size = size
        self.distance = 0

    def __str__(self):
        return '''This is a rock.
Rock Type: {}
Rock Texture: {}
Rock Color: {}
Rock Weight: {}
Rock Size: {}'''.format(self.type, self.texture, self.color, self.weight, self.size)

    def talk(self):
        print 'Rocks can\'t talk. What did you think would happen?'

    def get_distance(self):
        return self.distance

    def throw(self, strength):
        if self.distance == 0:
            print 'You throw the rock.'
            self.distance += strength
        else:
            print 'You can\'t throw something you don\'t have!'

    def force(self):
        print 'You use the Force to bring the rock back to you.'
        self.distance = 0
    
