import abc
import random
import time


# 利⽤⾯试对象的编程思想，实现下⾯的功能
# 1. ⼩明 体重 80kg
# 2. 每跑步⼀次 重量减去 0.5kg
# 3. 每吃⼀顿饭 重量增加 0.1kg
class Xiaoming():
    def __init__(self, weight):
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        return self.weight

    def eat(self):
        self.weight += 0.1
        return self.weight


d = Xiaoming(80)
print(d.run())
print(d.eat())


# ⽤⾯向对象的思维 实现下列需求
# 1. ⼠兵 都有 姓名和⼀把枪
# 2. ⼠兵 可以 ⽤枪开⽕
# 3. 枪 能都装填⼦弹
# 4. 枪 能够发射⼦弹
# 组合
class Gun:
    def __init__(self, guntype):
        self.guntype = guntype

    def fill(self):
        return "fill"

    def shoot(self):
        return "shoot"


class Soldier:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def fire(self):
        print(f"{self.name} use {self.gun.guntype} fire, which can {self.gun.fill()} and then {self.gun.shoot()}")


gun = Gun('AWK')
s = Soldier('Xiaoming', gun)
s.fire()


# 利⽤多态实现我上课说的不同的游戏⻆⾊出拳的例⼦
# 定义抽象类（继承抽象基类），定义抽象方法
class PlayGame(abc.ABC):
    @abc.abstractmethod
    def fight(self):
        pass


# 实现抽象方法
class A(PlayGame):
    def fight(self):
        print("角色A出拳A")


# 实现抽象方法
class B(PlayGame):
    def fight(self):
        print("角色B出拳B")


# 实例化
a = A()
b = B()
a.fight()
b.fight()


# # 函数调用
# def choosewho(obj):
#     obj.fight()
#
#
# choosewho(a)
# choosewho(b)


# 实现⼀个装饰器，每次调⽤函数时，将函数名字 和 调⽤时间写⼊到⽂件 a.txt 中
# 1. 要求先熟悉 python ⽂件的操作
# 2. 函数名可⽤ __name__ 来获取，如
# 3. 调⽤时间 可以熟悉 time 模块
def outer(func):
    def inner():
        start_time = str(time.time())
        var = func.__name__
        with open('a.txt', 'a') as file:
            file.write(f"函数名为{var},被调用时间为{start_time}\n")
        return func()
    return inner


@outer
def testdecorator():
    time.sleep(1)


testdecorator()


# ⽤python 模拟实现 扔1000次硬币，然后分别显示出掷出正⾯和反⾯的次数
# 提示：
# 正⾯，反⾯ 可以⽤ 0 或 1 来代替，然后统计 1000次中 1 和 0 出现的次数
def coinplay():
    count_0 = 0
    count_1 = 0
    while count_0 + count_1 < 1000:
        x = random.randint(0, 1)
        if x == 0:
            count_0 += 1
        else:
            count_1 += 1
    print(f"1000次中0出现了{count_0}次，1出现了{count_1}次")


coinplay()