import random

""" I know there are much easier ways to do this game in python,
although I wanted the result to look like this, I made it from scratch
also I tried to make the code as simple as I could, I really did enjoyed this
project, looking forward for the next...
Roni Miguel """

def draw_rock():
	"""ROCK  VS ROCK ART"""
	print ("""
               ____                ____
        ---"  _____)              (_____  "---
YOU: ROCK    (_____)              (_____)  PC : ROCK
             (_____)              (_____)
        ---.  (____)              (____)  .---
             "_(___)              (___)_"

It's a Draw\n					 """)
	
def draw_paper():
	"""PAPER VS PAPER ART"""

	print (""" 
              ______              ______    
        ---"    ____)___      ___(____    "---
YOU: PAPER       _______)    (_______      PC : PAPER
                 ________)  (________
        ---.   ________)      (________   .---
             "________)        (________"

It's a Draw\n					""")

def draw_scissors():
	"""SCISSORS VS SCISSORS ART"""
	
	print ("""    
              _____                _____
        ---"   ____)____      ____(____   "---
YOU: SCISSORS (_________)    (_________)   PC : SCISSORS
              (__________)  (__________)
        ---.  (____)              (____)  .---
            "_(___)                (___)"

It's a Draw\n					""")
	
def lose_rock_vs_paper():
	"""ROCK VS PAPER ART"""

	print ("""
               ____               ______            
        ---"  _____)          ___(____    "---  
YOU: ROCK    (_____)         (_______      PC : PAPER
             (_____)        (________
        ---.  (____)          (_______    .---
             "_(___)           (________"

You lose.\nPAPER covers ROCK\n """)

    
def win_rock_vs_scissors():
    """ROCK VS SCISSORS ART"""

    print ("""
               ____                _____            
        ---"  _____)          ____(___    "---  
YOU: ROCK    (_____)         (_________)   PC : SCISSORS
             (_____)        (__________)
        ---.  (____)              (____)   .---
             "_(___)              (____)"

You win!\nROCK crushes SCISSORS\n""")
	
def win_paper_vs_rock():
	"""PAPER VS ROCK ART"""

	print (""" 
              ______                  ____
        ---"    ____)___             (_____  "---
You: PAPER       _______)            (_____)  PC : ROCK
                 ________)           (_____)
        ---.   ________)             (____)  .---
             "________)              (___)_"

You win.\nPAPER covers ROCK\n""")


def lose_paper_vs_scissors():
    """PAPER VS SCISSORS ART"""

    print (""" 
              ______                  ____
        ---"    ____)___         ____(_____  "---
You: PAPER       _______)       (_________)   PC : SCISSORS
                 ________)     (__________)
        ---.   ________)             (____)  .---
             "________)              (____)_"
 
You lose!\nSCISSORS cuts PAPER\n""")
	
def lose_scissors_vs_rock():
	"""SCISSORS VS ROCK ART"""
	
	print ("""    
              _____                   ____
        ---"   ____)____             (_____  "---
You: SCISSORS (_________)            (_____)  PC : ROCK
              (__________)           (_____)
        ---.  (____)                 (____)  .---
            "_(___)                  (___)_"

You lose.\nROCK crushes SCISSORS\n""")

def win_scissors_vs_paper():
    """SCISSORS VS PAPER ART"""
    
    print ("""    
              _____                  ______     
        ---"   ____)____         ___(____    "---  
You: SCISSORS (_________)       (_______      PC : PAPER
              (__________)      (________
        ---.  (____)             (_______    .---
            "_(___)                (________"

You win!\nSCISSORS cuts PAPER\n""")


def welcome_msg():
	print ("""             
           WELCOME TO                
  ________ __________ _________     
 /        *          *         \    
|   ROCK  |   PAPER  | SCISSORS |   
 \________*__________*_________/    
		  """)

def main():
	
	#Get user input, get random number
	user = int(input('1 = ROCK | 2 = PAPER | 3 = SCISSORS : ')) 
	pc = random.randint(1,3)
	

	# check for winner
			
	if user == 1 and pc == 1:
		draw_rock()
			
	elif user == 2 and pc == 2:
		draw_paper()
			
	elif user ==3 and pc == 3:
	   draw_scissors()
			
	elif user == 1 and pc == 2:
		lose_rock_vs_paper() 
	
	elif user == 1 and pc == 3:
		win_rock_vs_scissors()
		
	elif user == 2 and pc == 1:
		win_paper_vs_rock()
		
	elif user == 2 and pc == 3:
		lose_paper_vs_scissors()
		
	elif user == 3 and pc == 1:
		lose_scissors_vs_rock()
		
	elif user == 3 and pc == 2:
		win_scissors_vs_paper()
		
	else:
		print('INVALID OPTION')
		main()		


welcome_msg()
main()

while True:
    again = input("1 = PLAY AGAIN or Press ENTER to EXIT: ")
    if again == '1':    # made this a string because if the user typed a letter 
        main()          # the game would crash

    else:
        break