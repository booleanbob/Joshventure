#Enemies List
from random import randint

class Enemy():
	def __init__(self, name, hp, damage, defense):
		self.name = name
		self.hp = hp
		self.ATK = 1
		self.atk1 = 0
		self.atk2 = 0
		self.spatk = 0
		self.defense = defense
		self.damage = damage
		self.descrip = 0
		self.alive = 1
		
	def enemyattack(self):
		atkchoice = randint(1,4)
		if atkchoice == 1:
			print(self.atk1)
			dmg_to_josh = randint(1,self.damage)
		elif atkchoice == 2:
			print(self.atk2)
			dmg_to_josh = randint(1,self.damage)
		elif atkchoice == 3:
			print(self.spatk)
			dmg_to_josh = randint(self.damage-1,self.damage+5)
		else:
			print(self.name + " tried to attack and missed!\n")
			dmg_to_josh = 0
		return dmg_to_josh


def gen_ginger():
	ginger = Enemy("Ginger", 100, 10, 5)

	ginger.descrip = '''
	You see a fearsome, wild Ginger. Her red hair crackles with
	magical energy, and she is licking her wizard staff with an inappropriate
	sexual fervor. She wears a torn linen skirt that shows her lithe legs, and
	her top is barely concealed by a tight leather bodice. In her left hand is 
	a bottle of 100 Year Old Jameson. You can LOOK at the bottle, TEASE ginger,
	LICK ginger, or SEX ginger.'''

	ginger.atk1 = "Ginger gets on the floor and attacks your ankles!\n"
	ginger.atk2 = "Ginger blasts you with her Wisconsin Molten Cheese Gun!\n"
	ginger.spatk = '''Ginger executes a devastating special attack. We can't say what it is, but
her mouth is open in that super wide way it always does
'''
	
	return ginger

gen_ginger()	



