#encoding:utf-8
import re
import math
s = '1+2*3-(5/6)+sin(45)-ln(100)+sin(45)  sin(45)'
str_sin = re.findall('sin\(\d*\)', s) #获取sin（45）
print (str_sin)
print(str_sin[1])
t=len(str_sin)
print(t)

s = re.sub('sin(\(\d*\))','22',s,t)  #替换
print(s)