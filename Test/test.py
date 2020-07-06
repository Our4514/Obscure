#encoding:utf-8
import re
import math
s = '1+2*3-(5/6)+sin(45)-ln(100)+sin(45)  sin(45)'
str_sin = re.search('sin(\(\d*\))', s).group() #获取sin（45）
print (str_sin)
num_sin = re.search('\d+', str_sin).group() #获取sin（45）中的45
print (num_sin)
re_sin = math.sin(int(num_sin)) #计算sin（45）
print (re_sin)
s = re.sub('sin(\(\d*\))',str(re_sin) ,s,1)  #替换
print(s)