"""牌面输入归一化与格式化工具。"""

# J/Q/K 与数字点数的双向映射
_JQK_TO_NUM = {'J': 11, 'j': 11, 'Q': 12, 'q': 12, 'K': 13, 'k': 13}
_NUM_TO_JQK = {11: 'J', 12: 'Q', 13: 'K'}

# 单次请求最多接受的牌数，防止恶意/误输入导致后端过载
MAX_CARD_COUNT = 30


def normalize_card_input(raw: str) -> list[int]:
    """把用户输入解析为点数整数列表。

    支持：
      - 空格、英文逗号、中文逗号分隔
      - J/j -> 11, Q/q -> 12, K/k -> 13
      - 自动过滤空项

    Args:
        raw: 用户原始输入字符串，例如 "1 2 J K" 或 "1,2,J,K"。

    Returns:
        点数整数列表，例如 [1, 2, 11, 13]。

    Raises:
        ValueError: 输入为空、包含非法字符或点数不在 1-13 范围时抛出中文错误。
    """
    if raw is None:
        raise ValueError('请输入牌面')

    # 统一替换分隔符为空格
    normalized = raw.replace('，', ' ').replace(',', ' ').replace('\n', ' ').replace('\t', ' ')
    # 合并连续空白
    while '  ' in normalized:
        normalized = normalized.replace('  ', ' ')
    normalized = normalized.strip()

    if not normalized:
        raise ValueError('请先输入牌面')

    tokens = normalized.split(' ')
    cards = []
    for token in tokens:
        if not token:
            continue
        if token in _JQK_TO_NUM:
            cards.append(_JQK_TO_NUM[token])
        else:
            try:
                value = int(token)
            except ValueError as exc:
                raise ValueError(f'输入格式错误："{token}" 不是合法的牌面（请使用 1-10 或 J/Q/K）') from exc
            if value < 1 or value > 13:
                raise ValueError(f'点数应在 1 到 13 之间，"{token}" 不合法')
            cards.append(value)

    if len(cards) > MAX_CARD_COUNT:
        raise ValueError(f'输入牌数过多，最多支持 {MAX_CARD_COUNT} 张')

    return cards


def format_card_value(value: int) -> str:
    """把点数整数格式化为牌面字符串。"""
    return _NUM_TO_JQK.get(value, str(value))


def format_solution_pair(group_a: list[int], group_b: list[int]) -> str:
    """把两个分组渲染为类似 `1+2 and 3+K` 的字符串。"""
    def group_to_str(group: list[int]) -> str:
        return '+'.join(format_card_value(v) for v in group)

    return f'{group_to_str(group_a)} and {group_to_str(group_b)}'


def format_combination(cards: list[int]) -> str:
    """把组合渲染为 `3+4+6` 形式。"""
    return '+'.join(format_card_value(v) for v in cards)
