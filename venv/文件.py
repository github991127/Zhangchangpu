'''
str = input("请输入：")
print(str)

fo = open("newfile.txt", "w")
print( "文件名: ", fo.name)
fo.write( "I like to rap!\nAnd you?\n")
fo.close()

fo = open("newfile.txt", "a")
fo.write( "of course.\n666")
fo.close()

try:
    fh = open("newfile", "r")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print ("Error: 写入文件失败")
else:
    print ("写入文件成功")
    fh.close()

fo = open("newfile.txt")#默认r，只读
str = fo.read(20)
print(str)
fo.close()

import os
#os.mkdir("新建文件夹")
print(os.getcwd())
'''
