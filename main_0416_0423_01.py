# ⽤python 模拟实现 扔1000次硬币，然后分别显示出掷出正⾯和反⾯的次数
# 提示：
# 正⾯，反⾯ 可以⽤ 0 或 1 来代替，然后统计 1000次中 1 和 0 出现的次数
import random


class Play:
    def __init__(self):
        pass

    def play(self):
        count_0 = 0
        count_1 = 0
        while count_0 + count_1 < 1000:
            a = random.randint(0, 1)
            if a == 0:
                count_0 += 1
            else:
                count_1 += 1
        print(f"0:{count_0},1:{count_1}")


c = Play()
c.play()



