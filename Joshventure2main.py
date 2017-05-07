#Joshventure 2 - Let's do this!

import os

# find out why this unicode doesn't work   tie = '\u22C8'
def cls(): 
	os.system("cls")

inventory = {}
inventory["Enchanted Top Hat"] = 1
inventory["Bowtie of Destiny"] = 0
inventory["Gingerbane"] = 1
inventory["Battle Axe"] = 0
inventory["Whiskey"] = 1

def header(heading):
	print("     >o< ~~ " + heading + " ~~ >o<     ")

def pregame_mod():
	pregame = 1
	while pregame:
		print("Here is a list of Options \nSelect Your Choice: \n ")
		print("For a Cast of Characters, enter 'Cast'")
		print("For a list of improvements made for this sequel, enter 'Improve'")
		print("For a list of alternative titles, enter 'Title'")
		print("To begin game, enter 'Begin'")
		pregame_choice = input("Please Enter Your selection:  ")
		pregame_choice.lower()
		cls()
		pgc = pregame_choice
		if pgc == "cast":
			print(" >o< ~~ Cast of Characters ~~ >o< ")
			print("Lord Elvanus, a Vengeful Elven Prince who is jealous of" +
			" Josh for copying his look")
			print("Our Hero, Josh, the lonely wanderer cast from his home for being too tall")
			print("The Mysterious Redhead, who cruelly stole Josh's magic bowtie" +
			" and banished him from the Broken City")
			print("Horatio, a Fool")
		elif pgc == "improve":
			print(" >o< ~~ improvements ~~ >o< ")
			print("You now have an inventory system, where you will carry several items, " +
			"many of which will be necessary to win.")
			print("You can now enter commands and directions instead of choosing from a list")
			print("You may have to fight enemies, using weapons!")
		elif pgc == "title":
			print(" >o< ~~ Alternative Titles ~~ >o< ")
			print("Joshventure 2: The Case of the Bowtie Burglar")
			print("Joshventure 2: Fancy Boy's Lament")
			print("Joshventure 2: Get a Haircut!")
			print("Joshventure 2: Cosplay Boogaloo")
		elif pgc == "begin":
			pregame = 0
			intro_mod()
			break
		else:
			print("That is not a valid selection, please try again!")
		
		if pregame == 1:
			input("Press Enter to return to Pregame Lobby ")
			cls()

def intro_mod():
	cls()
	print("Let's start the show")
	input("Press Enter to Get it On")
	cls()
	header("On Our Last Episode...")
	print("\n Josh was in a sleazy motel in Marrakesh after being exiled" +
	"from society due to tallness. \nHe received a mysterious telegram and journeyed " +
	"to Hungaria, where he made his way through a castle. \nHe received a scarlet bowtie " +
	"from an unknown benefactor, which he used to travel through a portal to the City " +
	"of Perdition. \nIn the city, he acquired an enchanted top hat and solved a riddle to discover the secret to unlocking a " +
	"vault, which contained a locked box. \nAmbushed by unknown assailants, Josh was saved by " +
	"a hooded figure, who pushed him through a tear in the Tesseract that was made by the opened " +
	"box. \nIn this swirling, disorienting dimension, The figure removed her hood to reveal " +
	"a beautiful but terrifying redheaded woman. \nHer sword deftly removed the scarlet bowtie " +
	"from Josh's neck, and she pushed him back through the tear. He awoke where he started, in " +
	"Marrakesh. \nHe wondered if any of it had been true, but then he saw the top hat beside the bed...\n\n")
	input("Press Enter to wake up")
	cls()
	
def hotel_mod():
	print("You are in your hotel room. The fetid stench of sub 3-star resorts " +
	"wafts through the air.\n The world is quiet outside.")
	print("There is a book on the table. Type READ BOOK to read it.")
	print("There is a door that leads into the hallway.")
	input("What would you like to do?")
	
	
	print("There is a mirror on the wall where you can check your stats. Typing LOOK")
	print("and the name of an object

print("Welcome to Joshventure 2: The Joshening!")
input("Press Enter to Continue |>o<|")
cls()

#maingame = 1

# while maingame:
pregame_mod()
intro_mod()
hotel_mod()
