#exciting intro again
import time

def wait(x):
		time.sleep(x)
		
t1 = """You are sitting at the edge of your bed after awakening
suddenly back in Marrakesh. The faint odor of sandlewood drifts through
the room and morning light trickles in through the crackes in the bent
window blinds. Your heart races as the sudden recollection of your previous
adventure somersaults through your mind. It would have been all too easy
to dismiss it as a dream, if it weren't for the top hat sitting next
to you on the bedside table. You pick up the top hat, turning events
over in your mind... 
"""

t2 = """
B A N G
on the door
 """
 
t3 = """
You jump up in alarm, top hat still in hand. The loud banging stops
and you reach toward the knob, nerves firing with excitement.
As you reach the knob...

"""

t4 = "B O O M !"

t5 = """
The door explodes! You are thrown back, but your agility
keeps you on your feet. Three men charge in, dressed in shiny
black silk tailed coats. They wear crooked stovepipe hats,
but strangely no ties. Two begin searching your room, while
the leader advances on you, drawing up a sinister umbrella. The
umbrella's handle is tarnished with red, its canopy looks burnt
with soot. The ferrule at the end looks suspiciously like the
barrel of a gun.

"""

t6 = '"Tell us where the bowtie is, and you may yet live," he scowls.\n'

t7 = 'You explain that the bowtie was taken from you by the red woman.'

t8 = """
"That's poor luck for you old chap. It was the one thing keeping
you alive."
"""

t9 = '"Why do you even want it? It was a nice bowtie, but..."'

t10 = """
"Fool!" he hisses, "That bowtie will grand supreme power to the one who
can wear it properly. We have battled the The Gentlemen's Confederation 
for it since time unknown. Now that they are all gone," he says, twisting 
his scowl into a smile, "it falls to us, the Society of Charlatans, to
put it to good use. 

"""

t11 = """
While you attempt to process this giant kerfuffle, the leader of the gang
steps toward you again and raises his umbrella gun to fire. Not knowing
what to do, you raise the top hat in your hands defensively.

"""

t12 = "\n B L A M ! \n"

t13 = """
Where once your hands held a top hat, there is now just a flying cloud
of debris, silk, and smoke. The hat must have had some impressive
anti-ballistic properties to have withstood the blast. 

Fluttering through the air is an antique playing card, the 
Queen of Spades. It must have been tucked inside the hat! You grab it.
"""

t14 = """
The card sails through the air for a half second, shimmers, and bursts
into a ball of light that surrounds you! Everything turns to mist and you
feel yourself falling...
"""

t15 = "\n falling..."

t16 = "\n still falling...."

t17 = "\n Really, quite a lot of falling. You glance at your watch."

t18 = """
Suddenly you alight on the ground. The mists still surround you, but they
begin to take on form and shade. The scene continues to resolve around you,
and you recognize the buildings from your last trip. You have returned to
The City. This time you will need all of your wits, your strength, and
your excessive height to conquer the challenges you face.

Are you ready for another Joshventure?
"""

t19 = "END OF INTRODUCTION"



def exciting_intro():	
	print(t1)
	wait(5)
	print(t2)
	wait(2)
	print(t2)
	wait(2)
	print(t3)
	print(t4)
	print(t5)
	print(t6)
	print(t7)
	print(t8)
	print(t9)
	print(t10)
	print(t11)
	print(t12)
	print(t13)
	
	go_on = 0
	while go_on == 0:
		print("This is your first chance for action. You can now 'THROW the CARD'")
		decision1 = input('>>>   ')
		decision1 = decision1.lower()
		if "throw" in decision1 and "card" in decision1:
			print(" \nYou throw the Queen of Spades at the attacker! \n")
			go_on = 1
		else:
			print("Maybe try that again? \n")

# exciting_intro()
