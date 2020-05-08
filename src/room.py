# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
	'''Room class'''

	def __init__(self, name, desc):
		self.name  = name
		self.desc  = desc
		self.exits = {}
		self.p     = None
		self.i     = None

