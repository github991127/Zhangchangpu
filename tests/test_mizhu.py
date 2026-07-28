"""Tests for source.mizhu."""

from source.mizhu import Solution


def test_find_num_basic():
    solver = Solution()
    result = solver.findNum([3, 4, 5, 6, 7, 8, 9, 13], 13)
    assert [3, 10] not in result  # 10 is not in input
    # 校验 13 单独成组
    assert [13] in result


def test_find_num_no_solution():
    solver = Solution()
    assert solver.findNum([1, 1, 1], 13) == []


def test_find_num_single_target():
    solver = Solution()
    assert solver.findNum([13], 13) == [[13]]


def test_find_num_deduplication():
    solver = Solution()
    # 2+2+2+2+2+1+1+1 = 13, 重复元素不应产生重复组合
    result = solver.findNum([2, 2, 2, 2, 2, 1, 1, 1], 13)
    assert len(result) == len({tuple(r) for r in result})
