"""张菖蒲模块 REST 接口。"""
from flask import Blueprint, jsonify, request

from source.zhangchangpu import match
from utils.cards import (
    format_solution_pair,
    normalize_card_input,
)

bp = Blueprint('zhangchangpu', __name__)


@bp.route('/zhangchangpu', methods=['POST'])
def zhangchangpu():
    """接收牌面列表，返回所有等和分组与最佳分组。"""
    data = request.get_json(silent=True) or {}
    raw = data.get('input', '')

    try:
        cards = normalize_card_input(raw)
    except ValueError as exc:
        return jsonify({'success': False, 'error': str(exc)}), 400

    p1, p2, length, longest = match(cards)

    # match 返回的 p1/p2 是字符串列表；若输入无解，第一个元素为人性化提示
    if not p2:
        return jsonify({
            'success': True,
            'data': {
                'input': cards,
                'input_count': length,
                'solutions': [],
                'best_solutions': [],
                'max_card_count': 0,
                'message': '这道题，会儿解不出来',
            }
        })

    return jsonify({
        'success': True,
        'data': {
            'input': cards,
            'input_count': length,
            'solutions': p1,
            'best_solutions': p2,
            'max_card_count': longest,
            'message': f'输入{length}个，获得{longest}个',
        }
    })
