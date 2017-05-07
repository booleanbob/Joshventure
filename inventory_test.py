#inventory test

inventory = {}
inventory["enchanted bowler hat"] = 1
inventory["Bowtie of Destiny"] = 0
inventory["Gingerbane"] = 1
inventory["Battle Axe"] = 0
inventory["Whiskey"] = 1

print(inventory)

print("")

for item in inventory:
	if inventory[item] == 1:
		print("you have 1 " + item)
