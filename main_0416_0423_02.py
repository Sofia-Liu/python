def lst_add(x, y):
    return x + y


def getwhat():
    a = [6, 1, 3]
    b = [5, 2, 7]
    i = 0
    c = []
    # for i in range(len(a))

    # method 1
    # while i < len(a):
    #     c.append(a[i] + b[i])
    #     i += 1
    # print(c)

    # method 2
    # c = list(map(lst_add, a, b))

    # method 3
    c = list(map(lambda x, y: x + y, a, b))
    print(c)
    # 列表、元组、字符串都是可迭代对象，可迭代：for


def calc():
    a = [2002, 2004, 1999, 2000, 1986, 1992]
    # 列表推导式
    b = [i for i in a if i % 4 == 0 or i % 400 == 0]
    print(b)


def test():
    lst = ['a', 'b', 'c', 'd']
    for index, value in enumerate(lst):
        print(index, value)
    # print(list(map(func, lst)))


def test1():
    score = [('aa', 90), ('bbbb', 89), ('ccc', 91)]
    # key是列表的下标 value是一个元组，对列表元组按元组的第二个元素排序
    # sorted是内置函数
    # out = sorted(score, key=lambda x: x[1], reverse=True)
    # print(out)
    # sort是序列属性
    score.sort(key=lambda x: x[1], reverse=True)
    print(score)


def test2():
    a = ['name', 'sex', 'age']
    b = ['kp', 'M', '20']
    # method1 内置函数zip
    c = dict(zip(a, b))
    # method2 循环赋值
    # c = dict()
    # for i in range(len(a)):
    #     c[a[i]] = b[i]

    print(c)


if __name__ == '__main__':
    # getwhat()
    # calc()
    # test()
    # test1()
    test2()