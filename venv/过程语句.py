

if True:
    print ("1")
    print ("2")
else:
    print ("3")
  #print ("4")# 没有严格缩进，在执行时会报错

num = 5
if num == 3:            # 无switch语句
    print ('boss')
elif num == 2:
    print ('user')
elif num == 1:
    print ('worker')
elif num < 0:
    print ('error')
else:
    print ('5')     # 条件均不成立时输出
    print (5)
print (5)
print ()

count = 3
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
   continue
   print ('No continue')
else:#循环执行完全部,else输出
   print ('No break')
print ()

for letter in 'nut':
    print('当前字母 :', letter)
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print('当前水果 :', fruit)
for index in range(len(fruits)):
   print ('当前水果 :', fruits[index])
   if index==2:break
else:print('No break')#循环执行完全部,else输出
