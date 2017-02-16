import time

inventory = {'matches':3,
             'dog':1,
             'grenade':100}

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
            if obj.lower() == 'key':
                if 'key' in inventory:
                    print 'You already have the key, idiot!'
                elif 'key' not in inventory:
                    print 'You pick up the key.'
                    inventory['key'] = 1
            elif obj.lower() == 'floorboards':
                print 'You scrape at them with your fingernails to no avail.'
            elif obj.lower() == 'crowbar':
                print 'Sorry. Wrong game.'
            else:
                print 'I cannot pick that up.'
        ###########################################################################################
        elif action.lower() == 'use':
            if obj.lower() == 'key':
                if 'key' not in inventory:
                    print 'You cannot use something that you do not have.'
                elif door_open == True:
                    print 'You just locked the door. You must really'
                    print 'like this room!'
                    door_open = False
                    print 'The key snaps off in the keyhole.'
                    del inventory['key']
                else:
                    print 'You stick the key in the keyhole. It is a '
                    print 'perfect fit. You hear the door unlock.'
                    door_open = True
            elif obj.lower() == 'grenade':
                print 'You lob a grenade at the door.'
                print 'It bounces off and rolls to your feet.'
                print 'You whisper "Oh d-" before being blown to smithereens.'
                break
            elif obj.lower() in ['matches', 'match']:
                if inventory['matches'] > 0:
                    print 'You light one of the matches. The room becomes'
                    print 'brighter for a minute, then you burn your finger'
                    print 'and the light goes out. Yeow!'
                    inventory['matches'] -= 1
                else:
                    print 'You are all out of matches. Way to be wasteful!'
            elif obj.lower() == 'door':
                if door_open:
                    print 'You turn the knob. It opens! You escape!'
                    break
                else:
                    print 'You turn the knob. Locked. Darn.'
        ###########################################################################################
        elif action.lower() == 'scream':
            print 'You yell at the top of your lungs. Nothing happens.'
            time.sleep(2)
            print 'Wait a minute...'
            time.sleep(2)
            print 'Something seems to be happening.'
            time.sleep(2)
            print 'You hear the click of an unlocking door.'
            door_open = True
        ###########################################################################################
        else:
            print 'Sorry, I didn\'t get that.'





































