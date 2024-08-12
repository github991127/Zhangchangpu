'''
4张牌，可以等和划分的概率
'''
def noMatch(a, b, c, d):
    if c == a + b or d == a + b or d == a + c or d == b + c or d == a + b + c or a + d == b + c:
        return 0
    else:
        return 1


def zcpFour():
    count = 0
    for a in range(1, 14):
        for b in range(a + 1, 14):
            for c in range(b + 1, 14):
                for d in range(c + 1, 14):
                    if noMatch(a, b, c, d):
                        count += 1
                        # print(a, b, c, d)  # 不可拿牌的组合
    count *= 24  # 组合*4！为排列

    print('总排列数：', 13 ** 4)
    print('可拿牌的排列数：', count)
    print('可拿牌的概率：', 1 - count / 13 ** 4)


if __name__ == '__main__':
    zcpFour()
