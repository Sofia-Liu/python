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


# ⽤冒泡排序实现 ⼀个⽆序列表的排序
# 冒泡排序原理：
# 每⼀趟只能确定将⼀个数归位。即第⼀趟只能确定将末位上的数归位，第⼆趟只能将倒数第
# 2 位上的数归位，依次类推下去。如果有 n 个数进⾏排序，只需将 n-1 个数归位，也就
# 是要进⾏ n-1 趟操作。
# ⽽ “每⼀趟 ” 都需要从第⼀位开始进⾏相邻的两个数的⽐较，将较⼤的数放后⾯，⽐较完毕
# 之后向后挪⼀位继续⽐较下⾯两个相邻的两个数⼤⼩关系，重复此步骤，直到最后⼀个还没
# 归位的数。
def bublesort(lst):
    lst = [1, 6, 3, 2, 5]
    for i in range(0, len(lst)):
        for j in range(1, len(lst) - i):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
        print(lst)


def bubble_sort_v3(array):
    # 最后一次元素交换的位置
    last_exchange_index = 0
    # 无序区的边界
    sort_boder = len(array) - 1
    for i in range(len(array) - 1):
        # 是否有序
        is_sorted = True
        for j in range(sort_boder):
            print(f'{array[j]}  和  {array[j + 1]}进行两两对比')
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_sorted = False
                last_exchange_index = j
        sort_boder = last_exchange_index
        if is_sorted:
            break
        print(f'第{i + 1}轮排序后，列表为 {array}')


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
    # bublesort([1, 6, 3, 2, 5])
    bubble_sort_v3([1, 6, 3, 2, 5])
    # get_min()
    # func(3, 5, 3)
