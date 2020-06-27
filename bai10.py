class myClass:
	def __init__(self):
		self.a = int(input("nhap a vao day:"))
		self.b = int(input("nhap b vao day:"))
		self.l = []
	def creatList(self):
		for i in range(0,self.a):
			self.l.append([])
			for j in range(0,self.b):
				self.l[i].append(i*j)
		print(self.l)
newClass = myClass()
newClass.creatList()
