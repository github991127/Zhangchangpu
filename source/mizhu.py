'''
输入数组，求所有 target 的组合
'''


class Solution:
    def __init__(self):
        self.index = []
        self.solution = set()

    def findNum(self, nums, target):
        # 特例
        if len(nums) == 1 and nums[0] == target:
            return [nums]
        elif len(nums) == 1:
            return []

        # 初始化
        self.index = [0] * len(nums)
        self.solution = set()
        nums = sorted(nums)

        self._try_next(0, nums, target, 0)
        return [list(combo) for combo in self.solution]

    def _try_next(self, i, nums, target, cur_sum):
        # 终止条件
        if cur_sum == target:
            temp = tuple(nums[j] for j in range(len(nums)) if self.index[j] == 1)
            if temp:
                self.solution.add(temp)
            return
        if i == len(nums) or cur_sum > target:
            return

        cur_sum += nums[i]
        if cur_sum <= target:
            self.index[i] = 1
            self._try_next(i + 1, nums, target, cur_sum)  # 采用此数字继续向后搜索，走左子树
            cur_sum -= nums[i]
        else:
            cur_sum -= nums[i]

        # 不采用此数字继续向后搜索，走右子树
        self.index[i] = 0
        self._try_next(i + 1, nums, target, cur_sum)


def main():
    obj = Solution()

    nums = [3, 4, 5, 6, 7, 8, 9, 13]
    target = 13

    x = obj.findNum(nums, target)
    for item in x:
        print(item)


if __name__ == '__main__':
    main()
