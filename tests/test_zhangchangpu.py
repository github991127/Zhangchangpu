"""Tests for source.zhangchangpu."""

from collections import Counter

import pytest

from source.zhangchangpu import get_solution, match


class TestGetSolution:
    def test_basic_solution(self):
        cards = [1, 2, 3, 5, 5, 6]
        solutions = get_solution(cards)
        assert len(solutions) > 0
        # 每一对分组应满足：和相等、均非空、使用的牌不超过输入（同一张牌不被两边共用）
        for group_a, group_b in solutions:
            assert sum(group_a) == sum(group_b)
            assert group_a and group_b
            used = list(group_a) + list(group_b)
            assert len(used) <= len(cards)
            for value in set(used):
                assert used.count(value) <= cards.count(value)

    def test_no_solution_odd_sum(self):
        # 单张牌时无法分成两个非空子集
        assert get_solution([1]) == []

    def test_no_solution_impossible(self):
        # 没有重复且无法拆分时无解
        assert get_solution([2]) == []

    def test_uses_partial_cards(self):
        # 允许只用部分牌：3+8+8+7+7 总和为奇数，但其中 7+8 == 7+8
        cards = [3, 8, 8, 7, 7]
        solutions = get_solution(cards)
        assert len(solutions) > 0
        for group_a, group_b in solutions:
            assert sum(group_a) == sum(group_b)
            assert group_a and group_b
            used = list(group_a) + list(group_b)
            assert len(used) <= len(cards)
            for value in set(used):
                assert used.count(value) <= cards.count(value)


class TestMatch:
    def test_match_returns_strings(self):
        p1, p2, length, longest = match([1, 2, 3, 5, 5, 6])
        assert all(isinstance(s, str) for s in p1)
        assert all(isinstance(s, str) for s in p2)
        assert length == 6
        assert longest == 6

    def test_no_solution_message(self):
        p1, p2, length, longest = match([1, 2, 4])
        assert p1 == ['这道题，会儿解不出来']
        assert p2 == []
        assert longest == 0

    def test_match_uses_format_solution_pair(self):
        p1, _, _, _ = match([1, 2, 11, 12])
        # 1+12 == 2+11
        assert any('1+Q' in s or 'Q+1' in s for s in p1)
