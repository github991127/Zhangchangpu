a,x,str,flag=1,2,'ab',False

list=[a,x,str,flag,9,'Z']#列表，变量
list.append('Y')
del list[0]
print(list)
print(list[1:3])
print(list[-3:-1])
print(list[2:])
print(list[2])
list[0]='OK'
print(list)
print()

tuple=(a,x,str,flag,9,'Z')#元组，常量
tuple2=()
tuple3=(3,)
print(tuple)
#tuple(o)='OK'  #error
print()

dict = {}#字典，无序，须先创建
dict["k1"] = "v1"
dict[2] = "v3"
dict[2] = "v2"
print(dict["k1"])  # 输出键为"k1" 的值
print(dict[2])# 输出键为 2 的值
del dict['k1']  # 删除键是'Name'的条目
dict.clear()      # 清空字典所有条目
del dict          # 删除字典

tinydict = {"k1": "v1", "k2": 2, True: False,"k2": "v2"}#键最多一个且为常量（数字，字符串或元组），重复时新键值取代老键值
print(tinydict)# 输出完整的字典
print(tinydict.keys())# 输出所有键
print(tinydict.values())# 输出所有值
