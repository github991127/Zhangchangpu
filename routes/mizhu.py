"""糜竺模块 REST 接口。"""
from flask import Blueprint, jsonify, request

from source.mizhu import Solution
from utils.cards import format_combination, normalize_card_input

bp = Blueprint('mizhu', __name__)


@bp.route('/mizhu', methods=['POST'])
def mizhu():
    """接收牌面列表，返回所有和为 13 的组合。"""
    data = request.get_json(silent=True) or {}
    raw = data.get('input', '')

    try:
        cards = normalize_card_input(raw)
    except ValueError as exc:
        return jsonify({'success': False, 'error': str(exc)}), 400

    solution = Solution()
    combinations = solution.findNum(cards, 13)

    if not combinations:
        return jsonify({
            'success': True,
            'data': {
                'input': cards,
                'target': 13,
                'combinations': [],
                'count': 0,
                'message': '这道题，冲儿解不出来',
            }
        })

    result = [
        {'cards': combo, 'text': format_combination(combo), 'sum': 13}
        for combo in combinations
    ]

    return jsonify({
        'success': True,
        'data': {
            'input': cards,
            'target': 13,
            'combinations': result,
            'count': len(result),
            'message': f'共找到 {len(result)} 种组合',
        }
    })
