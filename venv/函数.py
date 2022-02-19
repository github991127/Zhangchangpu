def fun1(a,b=0):#数、字符串、元组不可变（类似值传递）
   return a-b
if __name__=='__main__':#仅模块内调用
   c=fun1(2,3)
   print(c)
   c=fun1(2)
   print(c)
   c=fun1(b=2,a=3)
   print(c)
   print()

def fun2(a,*vartuple ):
   s=0
   for var in vartuple:
      s+=var
   return a*s
if __name__=='__main__':
   c=fun2(9,2,3,4,1)
   print(c)
   print()

fun1 = lambda arg1, arg2: arg1 + arg2
if __name__=='__main__':
   c=fun1(1,2)
   print(c)