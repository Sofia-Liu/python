# def multi(number):
#     j = 1
#     multi_each = 1
#     while j <= number:
#         multi_each *= j
#         j += 1
#     return multi_each


def sum_multi():
    num = int(input("请传入你想计算累乘和的整数："))
    print(num)
    # multi_list = []
    # for i in range(1, num+1):
    #     multi_list.append(multi(i))
    # print(f"传入整数的累乘和为{sum(multi_list)}")
    summ = 0
    for i in range(1, num + 1):
        multi_each = 1
        for j in range(1, i + 1):
            multi_each *= j
        summ += multi_each
    print(f"传入整数的累乘和为{summ}")


def is_huiwen():
    str_in = input("输入回文字符(含空格)：")
    print(str_in)
    # if str_in == str_in[::-1]:
    # reversed()返回迭代器对象
    if str_in == "".join(reversed(str_in)):
        print("是回文")
    else:
        print("不是回文")


def flower():
    for x in range(100, 1000):
        x_bai = int(x / 100)
        x_shi = int(x / 10) % 10
        x_ge = x % 10
        if x == (x_bai ** 3) + (x_shi ** 3) + (x_ge ** 3):
            print(x)


def bublesort(listt):
    i = 1
    while i < len(listt):
        if listt[i - 1] > listt[i]:
            temp = listt[i]
            listt[i] = listt[i - 1]
            listt[i - 1] = temp
        i += 1
    # print(listt)


def get_min():
    lst = [1, 3, 2, 4]
    bublesort(lst)
    print(f"{lst}的最小值为{lst[0]}")


def func(*num):
    lst = list(num)
    for i in set(lst):
        count = 0
        for j in lst:
            if i == j:
                count += 1
        print(f"数字{i}出现{count}次")


if __name__ == '__main__':
    # sum_multi()
    # is_huiwen()
    # flower()
    # bublesort([1, 3, 2, 5])
    # get_min()
    func(3, 5, 3)
