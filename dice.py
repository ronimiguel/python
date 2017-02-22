import random

	# draw the dice numbers on the screen
def side1 ():
	print ('.*****.')
	print (':     :')
	print (':  O  :')
	print (':     :')
	print (':.....:')

def side2 ():
	print ('.*****.')
	print (':O    :')
	print (':     :')
	print (':    O:')
	print (':.....:')

def side3 ():
	print ('.*****.')
	print (':O    :')
	print (':  O  :')
	print (':    O:')
	print (':.....:')

def side4 ():
	print ('.*****.')
	print (':O   O:')
	print (':     :')
	print (':O   O:')
	print (':.....:')

def side5 ():
	print ('.*****.')
	print (':O   O:')
	print (':  O  :')
	print (':O   O:')
	print (':.....:')

def side6 ():
	print ('.*****.')
	print (':O O O:')
	print (':     :')
	print (':O O O:')
	print (':.....:')

# print the dice 
def printRoll():
	# give the dice a random number
	dice = int(random.randint(1,6))

	# check wich side of the dice is up and print
	if dice == 1 :
		return side1()

	elif dice == 2 :
		return side2()

	elif dice == 3 :
		return side3()

	elif dice == 4 :
		return side4()

	elif dice == 5 :
		return side5()
	elif dice == 6 :
		return side6()

#prompt if the user wants to roll the dice again....
def rollAgain():
	
	while True:
		try:
			x = int(input('\nWould you like to roll the dice?\n\nPress 1 = YES\nPress 2 = Exit: '))
			if x == 1:
				printRoll()
				rollAgain()
		except ValueError:
			print ('\nINVALID OPTION')
			continue
		if x > 2:
			#Option for EXIT the program
			print ('\nINVALID OPTION')
			continue
		else:
			# x returned a valid number
			break

	# infinite user prompt, there is probably a much better way to right this, for now this works :)
	
# print the dice 1st roll
printRoll()
rollAgain()
