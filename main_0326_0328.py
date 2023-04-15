def exe_sorce():
    sorce = {'java': 90, 'python': 97, 'c#': 89}
    print(len(sorce))
    sorce['java'] = 95
    print(sorce)
    sorce['php'] = 90
    print(sorce)
    print('js' in sorce)
    val = sorce.values()
    print(max(val))
    for key, value in sorce.items():
        if value == max(val):
            print(key)


def exe_set():
    lst1 = [1, 2, 3, 5, 6, 3, 2]
    lst2 = [2, 5, 7, 9]
    # lst_comm = set()
    # lst1_only = set()
    # for i in lst1:
    #     if i in lst2:
    #         lst_comm.add(i)
    #     else:
    #         lst1_only.add(i)
    # print(lst_comm)
    # print(lst1_only)

    set1 = set(lst1)
    set2 = set(lst2)
    print(set1 & set2)
    print(set1 - set2)
    print(set1.difference(set2))


if __name__ == '__main__':
    # exe_sorce()
    exe_set()
