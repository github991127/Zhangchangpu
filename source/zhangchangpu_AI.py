'''
AI系统，三种模式选择拿走卡片的方案
'''
from zhangchangpu import *


# 数组补集
def A_minus_B(A, B):
    set_B = set(B)
    # 列表推导式，保留B中不在A中的元素
    A_minus_B = [x for i, x in enumerate(A) if x not in set_B or A[i:].count(x) > B.count(x)]
    return A_minus_B


def get_kind(kaka):
    res_kind = 0
    for res in kaka:
        if res > 0 and res < 4:
            res_kind += 1
    return res_kind


# 总和数量优先，相差数量优先
def easy(solution):
    kaka_card = []
    player_card = []
    max_length = 0
    # 获取方案的最大长度
    for i in range(len(solution)):
        max_length = max(max_length, len(solution[i][0]) + len(solution[i][1]))
    # 从最大长度的方案中进行比较,选择相差数量大的方案
    max_difference = -1
    for i in range(len(solution)):
        if (len(solution[i][0]) + len(solution[i][1]) == max_length):
            # 求绝对值
            if (abs(len(solution[i][0]) - len(solution[i][1])) > max_difference):
                max_difference = abs(len(solution[i][0]) - len(solution[i][1]))
                if (len(solution[i][0]) - len(solution[i][1]) >= 0):
                    kaka_card = solution[i][0]
                    player_card = solution[i][1]
                else:
                    kaka_card = solution[i][1]
                    player_card = solution[i][0]
    return player_card, kaka_card


# 卡片进入背包后，kaka1-3张的种类变多
def normal(solution, list, kaka):
    kaka_card = []
    player_card = []
    pre_kind = get_kind(kaka)
    res_difference = -10
    list_wastage = []
    kaka_preview = []

    for i in range(len(solution)):
        # 复制原始背包资源
        kaka_preview = kaka[:]
        kaka_solution = solution[i][0]
        player_solution = solution[i][1]

        # 预演背包变化
        get_kaka_preview(kaka_preview, kaka_solution, list, player_solution)
        # 获取背包新增种类
        post_kind = get_kind(kaka_preview)
        res_difference_temp = post_kind - pre_kind
        # 更新分配方案
        if res_difference_temp > res_difference:
            res_difference = res_difference_temp
            kaka_card = kaka_solution
            player_card = player_solution

        # 交换两行方案，重新比较
        kaka_preview = kaka[:]
        kaka_solution = solution[i][1]
        player_solution = solution[i][0]

        get_kaka_preview(kaka_preview, kaka_solution, list, player_solution)
        post_kind = get_kind(kaka_preview)
        res_difference_temp = post_kind - pre_kind
        if res_difference_temp > res_difference:
            res_difference = res_difference_temp
            kaka_card = kaka_solution
            player_card = player_solution

    print("背包新增类：", res_difference)
    return player_card, kaka_card


def get_kaka_preview(kaka_preview, kaka_solution, list, player_solution):
    list_wastage = A_minus_B(list, kaka_solution + player_solution)
    # 进入背包
    for res in kaka_solution:
        kaka_preview[res] += 1
    # 浪费自罚
    for wastage in list_wastage:
        if kaka_preview[wastage] > 0:
            kaka_preview[wastage] -= 1
    return kaka_preview


# 卡片进入背包后，kaka1-3张的种类变多，player1-3张的种类变少
def hard(solution, list, kaka, player):
    kaka_card = []
    player_card = []
    pre_kind = get_kind(kaka)
    pre_kind_player = get_kind(player)
    res_difference = -20
    list_wastage = []
    kaka_preview = []

    for i in range(len(solution)):
        # 复制原始背包资源
        kaka_preview = kaka[:]
        player_preview = player[:]
        kaka_solution = solution[i][0]
        player_solution = solution[i][1]

        # 预演背包变化
        get_kaka_preview(kaka_preview, kaka_solution, list, player_solution)
        # 获取背包新增种类
        post_kind = get_kind(kaka_preview)

        # 预演背包变化player
        get_player_preview(player_preview, player_solution)
        # 获取背包新增种类player
        post_kind_player = get_kind(player_preview)

        res_difference_temp = post_kind - pre_kind + pre_kind_player - post_kind_player

        # 更新分配方案
        if res_difference_temp > res_difference:
            res_difference = res_difference_temp
            kaka_card = kaka_solution
            player_card = player_solution

    print("背包新增类(减去玩家新增类)：", res_difference)
    return player_card, kaka_card

def get_player_preview(player_preview, player_solution):
    list_wastage = A_minus_B(list, player_solution + player_solution)
    # 获取前N/2的最多数量的种类
    # 进入背包
    for res in player_solution:
        player_preview[res] += 1

    return player_preview


def main():
    player = [1, 1, 3, 1, 3, 0, 0, 0, 0, 0]
    kaka = [0, 0, 0, 0, 0, 0, 3, 1, 3, 1]
    list = [1, 1, 1, 3, 5, 6, 6, 7, 8, 8]
    print_card(list)
    solution = get_solution(list)

    # player_card, kaka_card = easy(solution)
    # player_card, kaka_card = normal(solution, list, kaka)
    player_card, kaka_card = hard(solution, list, kaka, player)

    kaka_preview = get_kaka_preview(kaka, kaka_card, list, player_card)
    player_preview = get_kaka_preview(player, player_card, list, kaka_card)

    print("卡卡拿走的卡片：", kaka_card)
    print("卡卡的背包：", kaka_preview)
    print("玩家拿走的卡片：", player_card)
    print("玩家的背包：", player_preview)


if __name__ == "__main__":
    main()
