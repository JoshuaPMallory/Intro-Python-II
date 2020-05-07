import colorama

import ansiwrap

from player import Player
from room   import Room
from item   import Item


colorama.init()

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'] .exits.update({'north': room['foyer']})
room['foyer']   .exits.update({'south': room['outside']})
room['foyer']   .exits.update({'north': room['overlook']})
room['foyer']   .exits.update({'east' : room['narrow']})
room['overlook'].exits.update({'south': room['foyer']})
room['narrow']  .exits.update({'west' : room['foyer']})
room['narrow']  .exits.update({'north': room['treasure']})
room['treasure'].exits.update({'south': room['narrow']})

# Functions

def wprint(text, width = 80):
	'''Keeps all text in width.
	wprint(text, width = 80)

	text
		String of any length.

	width
		Integer, default 70.
	'''

	for item in ansiwrap.wrap(text, width = width, subsequent_indent = ' '):
		print(item)


def here():
	'''Shows all pertinent info for a place.

	Location name, description, any players and items, and exits.
	'''

	print()
	wprint(f'\033[1;33m{player.loc.name}\033[m')
	wprint(f'\033[0;33m{player.loc.desc}\033[m')

	if player.loc.p != None:
		wprint(player.loc.p)

	if player.loc.i != None:
		wprint(player.loc.i)

	exit_string = '\033[1;36;40m[ Exits: \033[00m'
	for thing in player.loc.exits:
		exit_string += f'\033[1;33;40m+{thing}\033[00m '
	exit_string = exit_string + '\033[1;36;40m]\033[00m'

	wprint(exit_string)


dict_dir = {'n'  : 'north'
           ,'s'  : 'south'
           ,'e'  : 'east'
           ,'w'  : 'west'
           ,'u'  : 'up'
           ,'d'  : 'down'
           ,'out': 'outside'
           ,'ne' : 'north east'
           ,'nw' : 'north west'
           ,'se' : 'south east'
           ,'sw' : 'south west'
           }


def parser(input):
	'''Terrible Parser
	Need to replace this with something that treats the input as a known command,
	that way we can just use a try statement and print the error at the end
	but also avoid the problem of getting so many if's running through everything.

	Mabe this needs to be a class?
	Just take in whatever and treat the first part as a function and the rest as arguments?
	'''

	# Quit
	if input.lower() in ('q' or 'quit'):
		print('See ya!')
		running = False

	# Look
	elif input.lower() in ('here', 'l', 'look', 'look here'):
		here()

	# Move
	elif input.lower() in ('n'   ,'north'
	            		  ,'s'   ,'south'
	            		  ,'e'   ,'east'
	            		  ,'w'   ,'west'
	            		  ,'u'   ,'up'
	            		  ,'d'   ,'down'
	            		  ,'out' ,'outside'
	            		  ,'in'
	            		  ,'ne'  ,'north east'
	            		  ,'nw'  ,'north west'
	            		  ,'se'  ,'south east'
	            		  ,'sw'  ,'south west'
	            		  ):
		input = input.lower()
		try:
			input      = dict_dir[input]
		except KeyError:
			pass

		try:
			player.loc = player.loc.exits[input]
			here()
		except KeyError:
			print(f'\033[1;31;40mYou can\'t go {input} here.\033[00m')

	# Speak
	elif input[:4].lower() == 'say ':
		print(f'{player.name} says, "{input[4:]}"')

	# Inventory
	elif input.lower() in ('i', 'inv', 'inventory'):
		if player.inv == []:
			print('Your pockets are empty.')
		else:
			print('-- Name ---\t-- Desc ---')
			for item in player.inv:
				print(f'{item.name}\t\t{item.desc}')

	# All else
	else:
		print('\033[1;31;40mINVALID COMMAND\033[00m')


# Make a new player object that is currently in the 'outside' room.
item1  = Item('Journal', 'A worn leather journal. A pen is attached to the side.', 1)
item2  = Item('Rocks', 'Just a bunch of rocks. What kind of person would carry that around?', 20)

player = Player('Dude', 'He abides.', room['outside'], [item1, item2])

# Write a loop that:
#
# [X] Prints the current room name
# [X] Prints the current description (the textwrap module might be useful here).
# [X] Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


# Start
print('This is a game!')
print('Made by Josh.')

here()

running = True
while running == True:
	user_input = input()

	parser(user_input)
