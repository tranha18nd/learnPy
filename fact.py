x = input("Nhập số cần tính: ")
def fact(x):
	if(x == 0):
		return 1
	return int(x)*fact(int(x) - 1)
print(fact(x))