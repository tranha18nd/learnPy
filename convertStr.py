input_str = input("Nhập chuỗi phân tách bằng dấy , :")
input_list = input_str.split(',')
input_list.sort(reverse = True)
str_new = ','.join(input_list)
print(str_new)
str_upper = str_new.upper()
print(str_upper)