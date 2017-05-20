#read a savefile
import json
'''
with open('inventorytest.txt', 'r') as save:
	inventory = json.load(save)


print(inventory["tophat"])

print(type(inventory))

atkmod = 7

joshstat = {
"HP": 105,
"DEF": 32+atkmod,
"ATK": 55,
"TALL": 9000
}

inventory = {
"superbooze": 1,
"tophat": 1,
"bowtie": 0,
"mug": 0,
"battleaxe": 1,
"defeated": ["ginger","timekeeper","Mr. Manners"]
}

savestate = {
"saveinv": inventory,
"savestat": joshstat
}

with open('jsontest.txt', 'w') as save:
	json.dump(savestate, save)
'''

with open('jsontest.txt', 'r') as loadsave:
	Q = json.load(loadsave)
	
inventory = Q["saveinv"]
stats = Q["savestat"]

print(inventory)
print(type(inventory))
