#the Josh class

class Joshclass:
	
	def _init_(self, name):
		self.name = name
		
	inventory = {}
	inventory["enchanted bowler hat"] = 1
	inventory["Bowtie of Destiny"] = 0
	inventory["Gingerbane"] = 1
	inventory["Battle Axe"] = 0
	inventory["Whiskey"] = 1
	
	def inventory_check():
		for item in Joshclass.inventory:
			if Joshclass.inventory[item] == 1:
				print("you have 1 " + item)
				
	
	
print(Joshclass.inventory["Gingerbane"])

Joshclass.inventory_check()

	
			
