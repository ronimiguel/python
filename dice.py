import random

	# draw the dice numbers on the screen
def side1 ():
	print ('.******')
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
def rollDice():
	# give the dice a random number
	dice = int(random.randint(1,6))

	# check dice result and and print it's side
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
		try: # there must be a better way to code this,maybe make userAnswer a Function
			userAnswer = int(input('\nWould you like to roll the dice?\n\nPress 1 = YES\nPress 2 = Exit: '))
			if userAnswer == 1:
				rollDice()
				rollAgain()
		except ValueError:
			print ('\nINVALID OPTION')
			continue
		if userAnswer > 2:
			#Option for EXIT the program
			print ('\nINVALID OPTION')
			continue
		else:
			# user returned a valid number
			break


rollDice()
rollAgain()
