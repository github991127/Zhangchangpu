'''
https://zhuanlan.zhihu.com/p/142907344

'''

#输入数组，返回布尔数组，表示每个数字是否可以由数组中的数字相加得到。
def out_sum(nums):
    listBool = [False] * 27
    listBool[0] = True
    for n in nums:
        # 记录当前数字和所有已存在结果的和
        for i in range(13, -1, -1):
            if listBool[i]:
                listBool[i + n] = True
                # if i + n == 13:  # 可以组成13立即返回
                #     return listBool
    return listBool

# 输入数组，返回布尔值，表示数组中的数字是否可以组成13
def bool_sum(nums):
    listBool = [False] * 27
    listBool[0] = True
    for n in nums:
        # 记录当前数字和所有已存在结果的和
        for i in range(13, -1, -1):
            if listBool[i]:
                listBool[i + n] = True
                if i + n == 13:  # 可以组成13立即返回
                    return True
    return False



def out_sum_ex():
    nums = [3, 3, 4, 7, 9, 9, 13, 13]
    listBool = out_sum(nums)
    print('可以组成的数字和有：', end=' ')
    for i in range(1, 27):
        if listBool[i]:
            print(i, end=' ')

def bool_sum_ex():
    nums = [3, 3, 4, 7, 9, 9, 13, 13]
    b = bool_sum(nums)




if __name__ == '__main__':
    # out_sum_ex()
    bool_sum_ex()