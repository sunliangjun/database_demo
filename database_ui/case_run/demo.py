# 快速排序

def quick_sort(data):
    """快速排序"""
    if len(data) >= 2:  # 递归入口及出口
        mid = data[len(data) // 2]  # 选取基准值，也可以选取第一个或最后一个元素
        left, right = [], []  # 定义基准值左右两侧的列表
        data.remove(mid)  # 从原始数组中移除基准值
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data


# 长整数相加
def long_int_sum(int_str_one, int_str_two):
    list_sum = []
    list_long, list_short = (list(int_str_one), list(int_str_two)) if len(int_str_one) > len(int_str_two) else (list(int_str_two), list(
        int_str_one))
    len_short = len(list_short)
    len_long = len(list_long)
    print(list_short)
    print(list_long)
    # 将不进行运算的数字首先添加到list_sum列表中，后面运算的再继续添加
    for index in range(len_short, len_long):
        list_sum.append(list_long[index])
    flag = 0
    for index in range(len_short - 1, -1, -1):
        if flag != 0:
            int_sum = int(list_short[index]) + int(list_long[index]) + 1
        else:
            int_sum = int(list_short[index]) + int(list_long[index])
        if int_sum >= 10:
            list_sum.insert(0, int_sum - 10)
            flag = 1
            if index == 0:
                list_sum.insert(0, 1)
        else:
            list_sum.insert(0, int_sum)
            flag = 0
    return list_sum


def a():
    list_a = [678, 89]
    list_b = [1, 3, 4, 5, 7]
    for index in range(len(list_b) - 1, -1, -1):
        list_a.insert(0, list_b[index])
    print(list_a)


def b():
    list_a = [1, 3, 5, 7, 9]
    length = len(list_a)
    for i in range(length - 1, -1, -1):
        print(list_a[i])


def c():
    str_a = "1232234"
    list_a = list(str_a)
    print(list_a)


if __name__ == '__main__':
    # c()
    # 长整数相加
    a_str = "12345661365456"
    b_str = "95632154748913546"
    list_sum = long_int_sum(a_str, b_str)
    print(list_sum)

    # 示例：
    # array = [2, 3, 5, 7, 1, 4, 6, 15, 5, 2, 7, 9, 10, 15, 9, 17, 12]
    # print(quick_sort(array))
