class myClass():
	"""docstring for myClass"""
	def __init__(self, a, b):
		self.a = int(a)
		self.b = int(b)
	def sum(self):
		print(self.a + self.b)
newClass = myClass(3, 4)
newClass.sum()

class Person:
 # Định nghĩa lớp "name"
 name = "Person"
# Code by Quantrimang.com
 def __init__(self, name = None):
 # self.name là biến instance
 	self.name = name

jeffrey = Person("Jeffrey")
print ("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print ("%s name is %s" % (Person.name, nico.name))