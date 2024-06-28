'''
输入数组，求所有target=13的组合
'''


class Solution:
    def __init__(self):
        self.index = []  # 标记当前位置元素是否选中
        self.solution = []

    def findNum(self, nums, summ):
        # 特例
        if len(nums) == 1 and nums[0] == summ:
            self.solution.append(nums)
            return
        elif len(nums) == 1:
            return

        # 初始化
        self.index = [0] * len(nums)
        self.solution = []
        nums.sort()

        self.tryNext(0, nums, summ, 0)
        return self.solution

    def tryNext(self, i, nums, target, curSum):
        # 终止条件
        if curSum == target:
            temp = []
            for i in range(len(nums)):
                if self.index[i] == 1:
                    temp.append(nums[i])
            if temp not in self.solution:  # 去重
                self.solution.append(temp)
            return
        if i == len(nums) or curSum > target:
            return

        curSum += nums[i]
        if curSum <= target:
            self.index[i] = 1
            self.tryNext(i + 1, nums, target, curSum)  # 采用此数字继续向后搜索，走左子树
            curSum -= nums[i]
        else:
            curSum -= nums[i]

        # 不采用此数字继续向后搜索，走右子树
        self.index[i] = 0
        self.tryNext(i + 1, nums, target, curSum)


def main():
    obj = Solution()

    s = [3, 4, 5, 6, 7, 8, 9, 13]
    target = 13

    x = obj.findNum(s, target)
    for i in x:
        print(i)


if __name__ == '__main__':
    main()
