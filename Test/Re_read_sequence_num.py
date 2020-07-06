# _*_ coding:utf-8 _*_
def get_math_line(source, keyword):
    # re chinese
    # 源文件编码需要指定
    source = source.decode('gb18030')
    pattern = '((\d)*).*' + keyword
    pattern = pattern.decode('utf-8')
    import re
    prog = re.compile(pattern)
    result = prog.search(source)
    return result.group(1) if result else None

with open('source.txt', 'rb') as src_file:
    with open('dest.txt', 'w') as dst_file:
        for line in src_file.readlines():
            val = get_math_line(line, '受到雾霾影响')
            if val:
                print (val)
            else:
                dst_file.write(line.strip('\n'))