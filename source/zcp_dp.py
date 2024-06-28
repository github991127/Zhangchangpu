'''
# https://zhuanlan.zhihu.com/p/225662903
输入数组，返回两个互斥的子数组，使得两个子数组的和相等
动态规划
'''
index = []
solution = []


def tryNext(i, s, summ, curSum):
    if i == len(s):
        if curSum == summ:
            temp1, temp2 = [], []
            for i in range(len(s)):
                if index[i] == 1:
                    temp1.append(s[i])
                else:
                    temp2.append(s[i])
            temp, temps = [], []
            temp.append(temp1)
            temp.append(temp2)
            temps.append(temp2)
            temps.append(temp1)
            if temp not in solution and temps not in solution:
                solution.append(temp)
        return
    curSum += s[i]
    if curSum <= summ:
        index[i] = 1
        tryNext(i + 1, s, summ, curSum)
        curSum -= s[i]
    else:
        curSum -= s[i]
    index[i] = 0
    tryNext(i + 1, s, summ, curSum)


def find(s, summ):
    if len(s) == 1:
        return
    curSum = 0
    index.clear()
    for i in range(len(s)):
        index.append(0)
    tryNext(0, s, summ, curSum)
    for i in range(len(s)):
        find(s[:i] + s[i + 1:len(s)], summ - s[i] / 2)


def match(s):
    s.sort()
    summ = sum(s) / 2
    find(s, summ)
    longest = 0
    if solution == []:
        print("no solution")
    else:
        for i in range(len(solution)):
            print("solution " + str(i + 1) + " is: " + str(solution[i][0]) + " and " + \
                  str(solution[i][1]))
            temp = len(solution[i][0]) + len(solution[i][1])
            if (temp > longest):
                longest = temp
        j = 1
        for i in range(len(solution)):
            if len(solution[i][0]) + len(solution[i][1]) == longest:
                print("best solution " + str(j) + " is:" + str(solution[i][0]) + \
                      " and " + str(solution[i][1]))
                j += 1


def main():
    s = [1, 2, 3, 5, 5, 6]
    match(s)


if __name__ == "__main__":
    main()