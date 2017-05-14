#Room class
import enemies

class Room():
	
	def __init__(self, name, directions):
		self.directions = directions
		self.name = name
	
	def directions_avail(self):
		print("You can go the following directions: ")
		print(self.directions)


class RoomA1(Room):
	
	def __init__(self, name, directions):
		
		self.name = name
		self.directions = directions
	
	room_description = ''' \nYou are standing in the middle of a large, open
	square, cobblestones beneath you and a blue sky above. Around you are
	short stucco buildings, their color worn away by the swift ocean breeze
	that continues to blow your hair in different directions '''
	
	self.characters = [Ginger.name, "A Hobo"]
	
	def getcharacters():
		for char in self.characters:
			print(char)
	
	
rooma1 = RoomA1("Stonewillow Square", ["East", "West"])		
	
def go_room_A1():
	print(rooma1.name)
	print(rooma1.room_description)
	rooma1.directions_avail()
	rooma1.getcharacters()
	
go_room_A1()
