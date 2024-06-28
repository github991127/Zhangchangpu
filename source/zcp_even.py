'''
和为偶数，分为两组，每组元素之和为一半【回溯法】
'''
import copy

s = [3, 3, 8, 6, 9, 12, 1]
curSum = 0
solution = []
index = []
summ = 0


def notIn(a, b):
    c = copy.deepcopy(b)
    temp = []
    for i in range(len(b)):
        for j in range(len(b[i])):
            temp.append(1 - b[i][j])
        c.append(temp[:])
        temp.clear()
    if a not in c:
        return True
    else:
        return False


def tryNext(i):
    global curSum
    global summ
    if i == len(s):
        if curSum == summ:
            if notIn(index, solution):
                solution.append(index[:])
        return
    curSum += s[i]
    if curSum <= summ:
        index[i] = 1
        tryNext(i + 1)
        curSum -= s[i]
    else:
        curSum -= s[i]
    index[i] = 0
    tryNext(i + 1)


def zcpBase(s):
    global summ
    for i in range(len(s)):
        summ += s[i]
        index.append(0)
    summ /= 2
    tryNext(0)
    return solution




if __name__ == "__main__":
    x=zcpBase(s)
    print("按照0和1分为两组")
    print(x)
    for i in range(len(solution)):
        print()
        print("solution " + str(i + 1) + " is:",end=' ')
        for j in range(len(solution[i])):
            if solution[i][j] == 1:
                print(s[j],end=' ')
        print("and",end=' ')
        for j in range(len(solution[i])):
            if solution[i][j] == 0:
                print(s[j],end=' ')