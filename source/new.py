from collections import Counter


def get_cards(player, list_to_draw):
    # 计算需要获取的牌数（向下取整的一半）
    target_cards = len(list_to_draw) // 2

    # 统计list_to_draw中每种牌的数量
    card_counts = Counter(list_to_draw)

    # 对card_counts进行排序，根据数量降序排列
    sorted_cards = sorted(card_counts.items(), key=lambda x: x[1], reverse=True)

    # 初始化一个列表来存储将要添加到player的牌
    drawn_cards = []

    # 遍历排序后的牌，选择足够数量的牌
    for card, count in sorted_cards:
        # 如果已经获取了足够的牌，则停止
        if len(drawn_cards) >= target_cards:
            break

            # 选择当前牌直到达到目标数量或当前牌已取完
        max_to_draw = min(count, target_cards - len(drawn_cards))
        drawn_cards.extend([card] * max_to_draw)

        # 返回抽取的牌
    return drawn_cards


if __name__ == "__main__":
    # 写一个函数get_cards(player, list)，输入两个参数，一个待取的牌列表list；一个已有列表player
    # 要求：从list中获取一半的牌（向下取整）到player，要求获取后的player，同一种牌越多越好(优先有更多的4张相同牌，然后优先有更多的3张相同牌，以此类推)

    # 测试用例1
    player1 = [2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7]  # 若按照桶计数法，[0, 0, 1, 1, 2, 2, 3, 3, 0, 0]
    list1 = [2, 2, 2, 4, 6, 8, 9, 1]
    # 将list1的4张牌[2, 2, 2, 6]加入player1中是最优解，2变为4张，6变为4张
    print(get_cards(player1[:], list1))  # 输出[2, 2, 2, 6]

    # 测试用例2
    player2 = [2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7]
    list2 = [2, 2, 2, 4, 6]
    # 将list2的2张牌[4, 6]加入player2中是最优解，4变为3张，6变为4张
    print(get_cards(player2[:], list2))  # 输出[4, 6]

    # 测试用例3
    player3 = [2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7]
    list3 = [2, 2, 2, 3, 6, 9]
    # 将list3的3张牌[2, 2, 6]加入player3中是最优解，2变为3张，6变为4张
    print(get_cards(player3[:], list3))  # 输出[2, 2, 6]
