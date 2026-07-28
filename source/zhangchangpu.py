'''
输入数组，返回两个互斥的子数组，使得两个子数组的和相等
回溯法
'''

from collections import defaultdict
from itertools import combinations

from utils.cards import format_solution_pair


def _get_solution(s):
    """返回所有满足 sum(A) == sum(B) 且 A、B 均非空的 [A, B] 分组。

    规则允许只用部分牌：从输入中选出互不相交的两个非空子集 A、B，
    满足 sum(A) == sum(B)，未使用的牌直接丢弃。

    实现思路：先枚举所有可能的和值 target，再对每个 target 用折半搜索
    （meet-in-the-middle）找出和为 target 的所有子集，最后两两配对去重。
    """
    s = sorted(s)
    n = len(s)
    if n < 2:
        return []

    # 枚举所有子集和，按和值分组保存（使用原数组中的下标集合作为子集标识）
    def enum_subsets(candidates):
        """返回 {subset_sum: [index_set, ...]}。"""
        m = len(candidates)
        mid = m // 2
        left, right = candidates[:mid], candidates[mid:]
        right_by_sum = defaultdict(list)
        for r in range(len(right) + 1):
            for combo in combinations(range(len(right)), r):
                subset_sum = sum(right[i] for i in combo)
                right_by_sum[subset_sum].append({mid + i for i in combo})
        result = defaultdict(list)
        for r in range(len(left) + 1):
            for combo in combinations(range(len(left)), r):
                left_sum = sum(left[i] for i in combo)
                left_set = set(combo)
                for right_set in right_by_sum.get(-left_sum, ()):
                    result[0].append(left_set | right_set)
                    # 上面这行是为了占位，下面会按真实 target 重新算；
                    # 更干净的做法是直接枚举所有子集和。
        return _enum_all_subsets(candidates)

    # 更直接：按每个可能的 target，用 meet-in-the-middle 找所有和为 target 的子集
    def subsets_with_sum(candidates, target):
        m = len(candidates)
        mid = m // 2
        left, right = candidates[:mid], candidates[mid:]
        right_by_sum = defaultdict(list)
        for r in range(len(right) + 1):
            for combo in combinations(range(len(right)), r):
                subset_sum = sum(right[i] for i in combo)
                right_by_sum[subset_sum].append({mid + i for i in combo})
        result = []
        for r in range(len(left) + 1):
            for combo in combinations(range(len(left)), r):
                left_sum = sum(left[i] for i in combo)
                need = target - left_sum
                left_set = set(combo)
                for right_set in right_by_sum.get(need, []):
                    full = left_set | right_set
                    if full:  # 非空
                        result.append(full)
        return result

    # 收集所有可能的 target（即所有非空子集的和），从小到大尝试
    all_targets = set()
    for r in range(1, n + 1):
        for combo in combinations(range(n), r):
            all_targets.add(sum(s[i] for i in combo))

    seen = set()
    result = []
    for target in sorted(all_targets):
        subsets = subsets_with_sum(s, target)
        # 两两配对，要求互不相交
        for i in range(len(subsets)):
            for j in range(i + 1, len(subsets)):
                if subsets[i] & subsets[j]:
                    continue
                group_a = [s[k] for k in sorted(subsets[i])]
                group_b = [s[k] for k in sorted(subsets[j])]
                key_a = tuple(group_a)
                key_b = tuple(group_b)
                key = (key_a, key_b) if key_a <= key_b else (key_b, key_a)
                if key not in seen:
                    seen.add(key)
                    result.append([group_a, group_b])
        # 一旦找到某个 target 的解，就只返回这个 target 下的所有解
        # 因为目标是“最多牌参与”，最小的 target 不一定牌最多，所以需要继续遍历
        # 但这里我们要保留所有 target 的解，由 match() 筛选最长
    return result


def _enum_all_subsets(candidates):
    """辅助函数：枚举 candidates 的所有非空子集，返回 {sum: [index_set, ...]}。"""
    m = len(candidates)
    result = defaultdict(list)
    for r in range(1, m + 1):
        for combo in combinations(range(m), r):
            subset_sum = sum(candidates[i] for i in combo)
            result[subset_sum].append(set(combo))
    return result


def _get_solution(s):
    """返回所有满足条件的 [A, B] 分组（允许未使用的牌）。"""
    s = sorted(s)
    n = len(s)
    if n < 2:
        return []

    # 枚举所有非空子集，按和分组
    subsets_by_sum = _enum_all_subsets(s)

    seen = set()
    result = []
    for target, subsets in subsets_by_sum.items():
        # 两两配对找不相交子集
        m = len(subsets)
        for i in range(m):
            for j in range(i + 1, m):
                if subsets[i] & subsets[j]:
                    continue
                group_a = [s[k] for k in sorted(subsets[i])]
                group_b = [s[k] for k in sorted(subsets[j])]
                key_a = tuple(group_a)
                key_b = tuple(group_b)
                key = (key_a, key_b) if key_a <= key_b else (key_b, key_a)
                if key not in seen:
                    seen.add(key)
                    result.append([group_a, group_b])
    return result


def get_solution(s):
    """外部可复用的求解接口，返回 [[groupA, groupB], ...] 原始解列表。"""
    return _get_solution(s)


def match(s):
    solution = _get_solution(s)
    length = len(s)
    longest = 0
    p1 = []
    p2 = []
    if not solution:
        p1 = ["这道题，会儿解不出来"]
        p2 = []
    else:
        for pair in solution:
            p1.append(format_solution_pair(pair[0], pair[1]))
            temp = len(pair[0]) + len(pair[1])
            if temp > longest:
                longest = temp
        for pair in solution:
            if len(pair[0]) + len(pair[1]) == longest:
                p2.append(format_solution_pair(pair[0], pair[1]))
    return p1, p2, length, longest


def print_card(card_list):
    p1, p2, length, longest = match(card_list)
    i = 1
    j = 1
    for i1 in p1:
        print(f"solution {i} is: ", end="")
        i += 1
        print("".join(i1))
    for i2 in p2:
        print(f"best solution {j} is:", end="")
        j += 1
        print("".join(i2))
    print(f"输入{length}个，获得{longest}个")


def main():
    card_list = [1, 2, 3, 5, 5, 6]
    print_card(card_list)


if __name__ == "__main__":
    main()
