'''
QIN 007 赵姬
设计人：菖蒲
武将称号：纵情恣欲
武将体力：3
挑朘：每名男性角色结束阶段，若其手牌数大于你，你可以依次展示其手牌直到展示牌点数不递增，然后你摸等同于展示牌数量张牌并交给其至多等量张牌，若展示牌点数之和大于你的体力值的十倍，你与其各回复1点体力。
囊扑：锁定技，当你受到伤害后，若你的手牌数全场最多，防止此伤害，然后来源弃置你两张牌。
求挑朘亮出牌的期望
'''
import random


def generate_until_increase(min_value=1, max_value=13):
    count = 0  # 记录生成的次数
    last_value = -1  # 上一次生成的值，初始化为-1
    while True:
        count += 1
        current_value = random.randint(min_value, max_value)  # 生成一个随机数
        # print(current_value)
        if current_value > last_value:
            last_value = current_value
        else:
            break
    return count


if __name__ == "__main__":
    N = 10000
    # N = 100
    x = 0
    for _ in range(N):
        count = generate_until_increase()
        x += count

    print("N =", N)
    print("挑朘亮出牌的期望值为：", x / N)
