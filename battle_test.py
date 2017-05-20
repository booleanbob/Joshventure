#Test Battle System!
import enemies
import joshclass
import time
from random import randint

def wait(x):
		time.sleep(x)
		
josh = joshclass.joshinst()

def hpbar():
	print(">o< HP: " + str(josh.CURHP) + " / " + str(josh.MAXHP) + " >o< ")

def fightround(enemy, josh):
	damtojosh = enemy.enemyattack()
	print(enemy.name + " does " + str(damtojosh) + " damage to Josh!")
	josh.CURHP -= damtojosh
	wait(1)
	damtoenemy = josh.heroattack()
	print("You do " + str(damtoenemy) + " to " + enemy.name)
	hpbar()
	input("Next?")

def battle_sys(enemy):
	blerg = enemy
	print("You draw your weapon and prepare to square off against a fearsome " + enemy.name + "!\n")
	print("Roll for Initiative! \n")
	go_first = randint(1,2)
	if go_first == 1:
		print("You go first! \n")
	if go_first == 2:
		print("Oh nooooo, " + enemy.name + " goes first! \n")
	fight = 1
	while enemy.hp > 0 and josh.CURHP > 0.2 * josh.MAXHP:
		fightround(blerg, josh)
	
			
		 

battle_sys(enemies.gen_ginger())



