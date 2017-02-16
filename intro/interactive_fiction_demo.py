inventory = {'matches':3,
             'dog':1,
             'hand_grenade':100}

def print_inventory(inv):
    print 'You have:'
    for i in inv:
        print '  {}: {}'.format(i.capitalize(), inv[i])

def game():
    print '''You find yourself in a locked room with a single door.
On the floor is a key.'''
    door_open = False
    while True:
        print
        command = raw_input('What would you like to do (Examine/Use/Pickup/Inventory)? ')
        print
        command = command.split()
        while len(command) < 2:
            command.append('') #Make sure that there are at least two 'words' in the list
        action, obj = command
        ###########################################################################################
        if action.lower() == 'inventory':
            print_inventory(inventory)
        ###########################################################################################
        elif action.lower() == 'examine':
            if obj.lower() == 'wall':
                print 'The walls look very wally. Through the fourth wall, you an see'
                print 'a class of programming students.'
            elif obj.lower() == 'floor':
                print 'The floor has not been washed in a long while.'
                if 'key' not in inventory:
                    print 'A single golden key lies on the floor.'
            elif obj.lower() == 'door':
                print 'It is clearly a door, meant for passing between two rooms.'
                print 'It has a keyhole.'
            elif obj.lower() == 'ceiling':
                print 'The cracks on the ceiling look suspiciously like Abraham Lincoln.'
            elif obj.lower() == 'matches':
                if inventory['matches'] > 0:
                    print 'Your matches are in your pocket, just waiting to be lit.'
                else:
                    print 'You have run out of matches. Sad!'
            else:
                print 'Sorry, I cannot see that.'
        ###########################################################################################
        elif action.lower() == 'pickup':
            pass
