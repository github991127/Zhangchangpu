'''
5张牌，可以等和划分的概率
'''
def noMatch(a, b, c, d):
    if c == a + b or d == a + b or d == a + c or d == b + c or d == a + b + c or a + d == b + c:
        return 0
    else:
        return 1


def zcpFive():
    count = 0
    for a in range(1, 14):
        for b in range(a + 1, 14):
            for c in range(b + 1, 14):
                for d in range(c + 1, 14):
                    for e in range(d + 1, 14):  # 判断第五个数能否和前四个数组成等式
                        if noMatch(a, b, c, d) and noMatch(a, b, c, e) and \
                                noMatch(a, b, d, e) and noMatch(a, c, d, e) and \
                                noMatch(b, c, d, e) and e != a + b + c + d and a + e != b + c + d and \
                                b + e != a + c + d and c + d != a + b + e and c + e != a + b + d and \
                                d + e != a + b + c:
                            count += 1
                            print(a, b, c, d, e)  # 不可拿牌的组合
    count *= 120
    print('总排列数：', 13 ** 5)
    print('不可拿牌的排列数：', count)
    print('可拿牌的概率：', 1 - count / 13 ** 5)


if __name__ == '__main__':
    zcpFive()
