"""Tests for utils.cards."""

import pytest

from utils.cards import (
    format_card_value,
    format_combination,
    format_solution_pair,
    normalize_card_input,
)


class TestNormalizeCardInput:
    def test_space_separated(self):
        assert normalize_card_input('1 2 J K') == [1, 2, 11, 13]

    def test_comma_separated(self):
        assert normalize_card_input('1,2,J,K') == [1, 2, 11, 13]

    def test_chinese_comma_separated(self):
        assert normalize_card_input('1，2，J，K') == [1, 2, 11, 13]

    def test_mixed_case_letters(self):
        assert normalize_card_input('j q k') == [11, 12, 13]

    def test_extra_whitespace(self):
        assert normalize_card_input('  1   2  J  ') == [1, 2, 11]

    def test_empty_string(self):
        with pytest.raises(ValueError, match='请先输入牌面'):
            normalize_card_input('')

    def test_none_input(self):
        with pytest.raises(ValueError, match='请输入牌面'):
            normalize_card_input(None)

    def test_invalid_token(self):
        with pytest.raises(ValueError, match='输入格式错误'):
            normalize_card_input('1 X 3')

    def test_out_of_range(self):
        with pytest.raises(ValueError, match='点数应在 1 到 13 之间'):
            normalize_card_input('0 14')

    def test_too_many_cards(self):
        with pytest.raises(ValueError, match='最多支持 30 张'):
            normalize_card_input(' '.join(['1'] * 31))


class TestFormatting:
    def test_format_card_value(self):
        assert format_card_value(1) == '1'
        assert format_card_value(11) == 'J'
        assert format_card_value(12) == 'Q'
        assert format_card_value(13) == 'K'

    def test_format_combination(self):
        assert format_combination([1, 11, 13]) == '1+J+K'

    def test_format_solution_pair(self):
        assert format_solution_pair([1, 2], [3, 13]) == '1+2 and 3+K'
