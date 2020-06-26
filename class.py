class myClass():
	"""docstring for myClass"""

	def __init__(self):
		self.arg = input("string in here :")
	def convert(self):
		print(self.arg.upper())
newClass = myClass()
newClass.convert()
		