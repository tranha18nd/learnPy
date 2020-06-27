class myClass():
	"""docstring for myClass"""

	def __init__(self):
		self.arg = input("string in here :")
	def convert(self):
		print(self.arg.upper())
	def binhphuong(self):
		print(int(self.arg)*int(self.arg))
newClass = myClass()
newClass.convert()
newClass.binhphuong()

		