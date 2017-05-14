class Room():
	
	def __init__(self, name, directions):
		self.directions = directions
		self.name = name
	
	def directions_avail(self):
		print("You can go the following directions: ")
		print(self.directions)

roomb1 = Room("Sunnybrook Hollow",["North","East","West","South"])

def go_room_b1():
	roomb1.directions_avail()

go_room_b1()
	
