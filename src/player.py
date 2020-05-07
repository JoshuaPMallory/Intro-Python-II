# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
	'''Player class'''

	def __init__(self, name, desc, loc, inv = []):
		self.name = name
		self.desc = desc
		self.loc  = loc
		self.inv  = inv

