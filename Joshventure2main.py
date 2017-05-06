#Joshventure 2 - Let's do this!

# find out why this unicode doesn't work   tie = '\u22C8'

print("Welcome to Joshventure 2: The Joshening!")
input("Press Enter to Continue |>o<|")
print("Here is a list of Options \nSelect Your Choice:")

pregame = TRUE
while pregame == TRUE:
	print("For a Cast of Characters, enter 'Cast'")
	print("For a list of improvements made for this sequel, enter 'Improve'")
	print("For a list of alternative titles, enter 'Title'")
	print("To begin game, enter 'Begin'")
	pregame_choice = input("Please Enter Your selection:")
	pregame_choice.lower()
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
	elif pgc == "

