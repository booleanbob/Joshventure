#the Josh class
from random import randint
class Joshclass():
	
	def __init__(self, name):
		self.name = name
		
	MAXHP = 50
	ATK = 10
	DEF = 10
	STR = 14
	DEX = 14
	CON = 18
	WIS = 9
	CHA = 11
	WPN = 15
	
	damage = ATK + WPN + STR
	CURHP = 50
	atk1 = "You attack mightily!"
	atk2 = "You attack sluggishly!"
	
	def heroattack(self):
		atkchoice = randint(1,4)
		if atkchoice == 1:
			print(self.atk1)
			dmg_to_enemy = randint(1,self.damage)
		elif atkchoice == 2:
			print(self.atk2)
			dmg_to_enemy = randint(1,self.damage)
		elif atkchoice == 3:
			print(self.spatk)
			dmg_to_enemy = randint(self.damage-1,self.damage+5)
		else:
			print("You tried to attack and missed!\n")
			dmg_to_enemy = 0
		return dmg_to_enemy
		
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
				
	
	
#print(Joshclass.inventory["Gingerbane"])

#Joshclass.inventory_check()

def joshinst():
	josh_instance = Joshclass("Josh")
	josh_instance.spatk = '''You pelt the enemy with figurines and other
things you should be embarrassed to own!
'''
	return josh_instance
				
