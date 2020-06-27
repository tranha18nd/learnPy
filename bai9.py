import math
# class caculator:
# 	def __init__(self, c, d, h):
# 		self.c = int(c)
# 		self.d = int(d)
# 		self.h = int(h)
# 	def cal(self):
# 		return math.sqrt(self.c*self.d*2/self.h)
# myCaculator = caculator(4,5,6)
# print(round(myCaculator.cal()))

class caculator :
	def __init__(self):
		self.a = int(input("nhap a :"))
		self.b = int(input("nhap b :"))
		self.c = int(input("nhap c :"))
	def cal(self):
		return math.sqrt(self.a*self.b*2/self.c)
myCaculator = caculator()
print(round(myCaculator.cal()))