#encoding:utf-8

s = "i13love14you520"
new_str = ""  		#创建一个空字符串
for ch in s:
	if ch.isdigit():		#字符串中的方法，可以直接判断ch是否是数字
		new_str += ch
	else:
		new_str += " "
sub_list = new_str.split()   #对新的字符串切片
num_list = list(map(int, sub_list)) 	#map方法，使列表中的元素按照指定方式转变
res  =sum(num_list)
print(num_list[1])
