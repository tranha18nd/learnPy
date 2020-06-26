arr = []
for x in range(2000,3201):
	if x%7 == 0 and x%5 != 0:
		arr.append(x)
# print(arr)
str = ', '.join(str(e) for e in arr)
print(str)
# for x in arr:
# 	print(x, ',')