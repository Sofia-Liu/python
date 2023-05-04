from collections import Counter


# 实现选择排序
# 实现原理：
# 　设第⼀个元素为⽐较元素，依次和后⾯的元素⽐较，⽐较完所有元素找到最⼩的元素，将
#   它和第⼀个元素互换
# 　重复上述操作，我们找出第⼆⼩的元素和第⼆个位置的元素互换，以此类推找出剩余最⼩
# 元素将它换到前⾯，即完成排序
# 算法描述：
# 1. 在⼀个⻓度为 N 的⽆序数组中，第⼀次遍历 n-1 个数找到最⼩的和第⼀个数交换。
# 2. 第⼆次从下⼀个数开始遍历 n-2 个数，找到最⼩的数和第⼆个数交换。
# 3. 重复以上操作直到第 n-1 次遍历最⼩的数和第 n-1 个数交换，排序完成。
def selsort():
    # lst = [2, 5, 1, 6, 9, 0]
    lst = [1, 6, 3, 2, 5]
    print(f"before:{lst}")
    # i=[0,5]  len=6
    # i = 0, j = [1, 5]
    # i = 1, j = [2, 5]
    # ...
    # i = 5, j = [6, 5]
    # for i in range(0, len(lst)):
    #     for j in range(i + 1, len(lst)):
    #         if lst[j] < lst[i]:
    #             lst[i], lst[j] = lst[j], lst[i]
    # 修改后
    for i in range(0, len(lst)):
        index_min = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[index_min]:
                index_min = j
        if index_min != i:
            lst[i], lst[index_min] = lst[index_min], lst[i]
    print(f"after:{lst}")


# selsort()


# 实现⽤户登录系统，⽤户名密码正确，提示登录成功，
# ⽤户名密码不匹配，提示密码错误，你还有⼏次登录机会
# 当⽤户输⼊三次密码时，提示不能登录,
# ⽤户名，密码存放在字典中 user_dict= {"cc":"123123","⼩⽜":"123123"}
# def jst(in_dict, user_dict):
#     flag = False
#     for key, value in user_dict:
# def usr_input():


def login():
    user_dict = {"cc": "123123", "小牛": "123456"}
    count = 3
    print("账号为：")
    x = input()
    print(x)
    while count > 0:
        # 输入密码
        print("输入密码为：")
        y = input()
        print(y)
        # 判断密码是否正确，正确打印成功，错误打印失败，允许重新输入，最多三次
        if user_dict[x] == y:
            print("密码正确，登录成功")
            break
        else:
            count -= 1
            if count != 0:
                print("密码错误,请重新输入（最多三次）")
            else:
                print("密码连续三次错误，无法登录")


# login()


# 有⽂件 a.txt(内容不为空，且有多⾏)
# 要求：找出出现次数最多的字符
def most_str():
    # method 1
    # 将文件内容拼接成字符串，每个字符及次数放到字典，将键值对按值大小降序排序，第一个键为出现次数最多的字符
    a = ''
    with open('a.txt', 'r') as file:
        for line in file:
            a += line
    print(f"文件内容为:\n{a}")
    # da = {}
    # for i in a:
    #     if i in da:
    #         da[i] += 1
    #     else:
    #         da[i] = 1
    # # print(da)
    # # da.__delitem__('\n')
    # # print(da)
    # da_sorted = sorted(da.items(), key=lambda x: x[1], reverse=True)
    # print(f"出现次数最多的字符为{da_sorted[0][0]}，共出现{da_sorted[0][1]}次")

    # method 2
    # 将文件内容拼接成字符串，用计数类中的most_common()方法对元素按出现次数降序排序,返回列表，列表的每个元素为元组（元素，次数）
    counter = Counter(a)
    lst = counter.most_common()
    print(f"出现次数最多的字符为{lst[0][0]}，共出现{lst[0][1]}次")


most_str()


# 实现算法，找出 列表中第⼆⼤的数,
# 如列表 [3,5,2,8,4,7,9] 第⼆⼤的数是 8
def sec():
    lst = [3, 5, 2, 8, 4, 7, 9]
    # method 1
    # lst.sort(reverse=True)
    # print(f"{lst}列表中第二大的数是{lst[1]}")

    # method 2
    # lst2 = sorted(lst, reverse=True)
    # print(f"{lst}列表中第二大的数是{lst2[1]}")

    # 修改后
    # method 3
    for i in range(0, len(lst)):
        index_max = i
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[index_max]:
                lst[index_max], lst[j] = lst[j], lst[index_max]
        if index_max != i:
            lst[index_max], lst[i] = lst[i], lst[index_max]
    print(f"排序后为{lst}，列表中第二大的数是{lst[1]}")

    # method 4
    # for i in range(0, len(lst)):
    #     for j in range(1, len(lst) - i):
    #         if lst[j - 1] < lst[j]:
    #             lst[j - 1], lst[j] = lst[j], lst[j - 1]
    # print(f"{lst}列表中第二大的数是{lst[1]}")

sec()
# ⾃习部分
# 1. 掌握 python 中的⽂件操作
