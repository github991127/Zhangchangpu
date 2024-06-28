'''
# https://zhuanlan.zhihu.com/p/225662903
输入数组，返回两个互斥的子数组，使得两个子数组的和相等
回溯法
'''
index = []
subIndex = []
solution = []
subSolution = []


def realSolution():
    real = []
    for i in range(len(solution)):
        temp1 = solution[i][0]
        temp2 = solution[i][1]
        if [temp1, temp2] not in real and [temp2, temp1] not in real:
            real.append(solution[i])
    solution.clear()
    for j in range(len(real)):
        solution.append(real[j])


def tryNext(i, subs, summm, curSumm):
    if i == len(subs):
        if curSumm == summm:
            temp = []
            for j in range(len(subs)):
                if subIndex[j] == 1:
                    temp.append(subs[j])
            if temp != []:
                subSolution.append(temp)
        return
    curSumm += subs[i]
    if curSumm <= summm:
        subIndex[i] = 1
        tryNext(i + 1, subs, summm, curSumm)
        curSumm -= subs[i]
    else:
        curSumm -= subs[i]
    subIndex[i] = 0
    tryNext(i + 1, subs, summm, curSumm)


def pre(s, curSum):
    get = []
    subs = []
    subIndex.clear()
    subSolution.clear()
    for j in range(len(s)):
        if index[j] == 0:
            subs.append(s[j])
            subIndex.append(0)
        else:
            get.append(s[j])
    summm = curSum
    curSumm = 0
    tryNext(0, subs, summm, curSumm)
    if subSolution != []:
        for k in range(len(subSolution)):
            t = []
            t.append(get[:])
            t.append(subSolution[k][:])
            if t not in solution:
                solution.append(t)


def outTryNext(i, s, summ, curSum):
    if i != len(s):
        curSum += s[i]
        if curSum <= summ:
            index[i] = 1
            pre(s, curSum)
            outTryNext(i + 1, s, summ, curSum)
            curSum -= s[i]
        else:
            curSum -= s[i]
        index[i] = 0
        outTryNext(i + 1, s, summ, curSum)
    else:
        pre(s, curSum)
        return


def match(s):
    s.sort()
    summ = sum(s) / 2
    curSum = 0
    for i in range(len(s)):
        index.append(0)
    outTryNext(0, s, summ, curSum)
    longest = 0
    realSolution()
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