import os
test_url='/home/zhangmeng/文档/PycahrmProject/project1/Ethraffle_v4b.dot'
file = open(test_url,"r")
for num,value in enumerate(file):
    print ("the nume:%s,the value is %s" %(num,value))
file.close()