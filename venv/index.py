
a,x,str,flag=2,1.5,'abcdefg',False

'''
a,x,str,flag=2,1.5,'abcdefg',False
list=(a,x,str,flag)
y=1.5
list1=[a,x,str,flag]
list2=[a,x,str,flag]

print(id(list1[1])==id(y))
print(id(list1)==id(list2))
print('hello world？?')
#print('单行注释')

print(a,x,str,flag)
print(type(a),type(x),type(str),type(flag))#获取类型

b=c=d=2#多变量赋值
c=3;d=4#单行多语句；；；
print(a,b,c,d)

print(str[1:3]+'23')#左索引起始0，含左
print(str[-3:-1])#右索引起始-1，含左
print(str[2:])
print(str[2])

b=a**x#幂运算
print(b)
b=x**a
print(b)
b=a//x#整除运算 - 返回商的整数部分（向下取整）4.5=4,-4.5=-5
print(b)
b=x//a
print(b)

a=60        # 60 = 0011 1100
b=13        # 13 = 0000 1101
c = a & b;  # 12 = 0000 1100
print(c)
c = a | b;  # 61 = 0011 1101

c = a ^ b;  # 49 = 0011 0001

c = ~a;     # -61 = 1100 0011

c = a << 2;  # 240 = 1111 0000

c = a >> 2;  # 15 = 0000 1111

c = a and b#如果 a 为 False，a and b 返回 False，否则它返回 b 的计算值

c = a or b#如果 a 是非 0，它返回 a 的值，否则它返回 b 的计算值

c = not(a)#如果 a 为 True，返回 False 。如果 a 为 False，它返回 True

c=a in list#值比较

c=a not in list

c=a is list[0]#取地址id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False

c=a is not list[0]

pass

print ('\\n')
print ('\n')
print (r'\n')

print ("My name is %s and weight is %d kg!" % ('Zara', 55))
'''