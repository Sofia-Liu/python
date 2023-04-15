import math
import random


def guess_num1():
    ans = 99
    count = 0
    while count < 3:
        try:
            user = int(input("please input your number:"))
            print(f"{user}\n")
            if user == ans:
                print("clever")
                break
            count += 1
        except ValueError:
            print("error type, please input int type number")
    if user != ans:
        print("stupid")


def guess_num2():
    ans = 99
    # flag = 1
    for i in range(3):
        user = int(input("please input a guess number within three times:"))
        if user == ans:
            print("clever")
            # flag = 0
            break
    # if flag:
    # 如果循环被break打断，else语句不会执行。
    else:
        print("stupid")


def whichdate():
    monlist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    user = input("YYYY-MM-dd：")
    year, mon, day = user.split('-')
    date = 0
    for i in range(int(mon) - 1):
        date += monlist[i]
    date += int(day)
    print(f"{user}对应第{date}天")


def multitable():
    for i in range(1, 10):
        str_i = ""
        for j in range(1, i + 1):
            str_i += " " + f"{i}*{j}={i * j}"
        print(str_i)


def reverse_multitable():
    for i in range(1, 10):
        str_i = ""
        for j in range(1, 11 - i):
            str_i += " " + f"{10 - i}*{11 - i - j}={(10 - i) * (11 - i - j)}"
        print(str_i)


def primenum():
    primenum_list = []
    for i in range(101, 201):
        flag = 0
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                flag += 1
        if flag == 0:
            primenum_list.append(i)
    print(set(primenum_list))


def handgame():
    robot = random.randint(0, 2)
    human = int(input())
    # print(type(int(human)))
    rule = ['石头', '剪刀', '布']
    print("human:%d %s" % (human, rule[human]))
    print("robot:%d %s" % (robot, rule[robot]))
    if human == 0:
        if robot == 0:
            print("石头平局")
        elif robot == 1:
            print("你（石头）赢了")
        else:
            print("你（石头）输了")
    elif human == 1:
        if robot == 0:
            print("你（剪刀）输了")
        elif robot == 1:
            print("剪刀平局")
        else:
            print("你（剪刀）赢了")
    else:
        if robot == 0:
            print("你（布）赢了")
        elif robot == 1:
            print("你（布）输了")
        else:
            print("布平局")


def handgame2():
    rule = ['石头', '剪刀', '布']
    pos_list = [(0, 1), (1, 2), (2, 0)]
    res = ["赢", "输"]
    count = 0
    while count < 5:
        robot = random.randint(0, 2)
        human = int(input("输入0或1或2\n"))
        if robot == human:
            print(f"robot出{rule[robot]} human出{rule[human]}:平局")
        else:
            for ele in pos_list:
                if ele[0] == robot and ele[1] == human:
                    print(f"robot出{rule[robot]} human出{rule[human]}:human{res[1]}")
                elif ele[0] == human and ele[1] == robot:
                    print(f"robot出{rule[robot]} human出{rule[human]}:human{res[0]}")
        count += 1


if __name__ == '__main__':
    # guess_num1()
    guess_num2()
    # whichdate()
    # multitable()
    # reverse_multitable()
    # primenum()
    # handgame()
    # handgame2()
