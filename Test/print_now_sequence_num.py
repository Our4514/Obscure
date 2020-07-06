import sys

def Local_file_sequence_num(): #获取当前的所在行数
    print ("here is :",__file__,sys._getframe().f_lineno)
    print(__file__)
    print(sys._getframe().f_lineno)
