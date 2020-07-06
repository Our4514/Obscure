#encoding:utf-8

import os

test_url='/home/zhangmeng/文档/PycahrmProject/project1/Ethraffle_v4b.dot'
def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    all_the_text = open(file_path).read()
    print(type(all_the_text))
    print(all_the_text)

read_file_as_str(test_url)
