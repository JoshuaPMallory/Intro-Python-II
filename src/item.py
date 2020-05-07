class Item():
	'''Item class'''

	def __init__(self, name, desc, weight):
		self.name   = name
		self.desc   = desc
		self.weight = weight
	
	def __str__(self):
		return self.name