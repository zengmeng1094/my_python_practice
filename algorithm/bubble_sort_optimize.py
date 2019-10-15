# 这里对冒泡排序进行深入理解，从实现冒泡到逐步优化


def bubble_sort(unsorted_list):
    # 原始的冒泡排序
    print("unsorted list : {}".format(unsorted_list))

    n = len(unsorted_list)
    count = 0
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            count += 1
            if unsorted_list[j] > unsorted_list[j+1]:
                tmp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j+1]
                unsorted_list[j+1] = tmp

    print("sorted list : {}".format(unsorted_list))
    print("sorted number : {}".format(count))


def bubble_sort_with_mark(unsorted_list):
    # 带标记位的冒泡
    print("unsorted list : {}".format(unsorted_list))

    n = len(unsorted_list)
    count = 0
    for i in range(0, n - 1):
        flag = True
        for j in range(0, n - 1 - i):
            count += 1
            if unsorted_list[j] > unsorted_list[j + 1]:
                tmp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j + 1]
                unsorted_list[j + 1] = tmp
                flag = False
        if flag:
            break

    print("sorted list : {}".format(unsorted_list))
    print("sorted number : {}".format(count))


def bubble_sort_with_boundary(unsorted_list):
    # 带需要比较边界的冒泡
    print("unsorted list : {}".format(unsorted_list))

    n = len(unsorted_list)
    count = 0
    boundary = n - 1
    for i in range(0, n - 1):
        flag = True
        for j in range(0, boundary):
            count += 1
            if unsorted_list[j] > unsorted_list[j + 1]:
                tmp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j + 1]
                unsorted_list[j + 1] = tmp
                flag = False
                boundary = j
        if flag:
            break

    print("sorted list : {}".format(unsorted_list))
    print("sorted number : {}".format(count))


def cocktail_sort(unsorted_list):
    # 从左到右排列再从右到左
    print("unsorted list : {}".format(unsorted_list))
    n = len(unsorted_list)
    count = 0

    for i in range(0, int(n//2)):
        is_sorted = True
        for j in range(i, n - 1 - i):
            count += 1
            if unsorted_list[j] > unsorted_list[j + 1]:
                tmp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j + 1]
                unsorted_list[j + 1] = tmp
                is_sorted = False
        if is_sorted:
            break
        is_sorted = True
        for j in range(n - 1 - i, i, -1):
            count += 1
            if unsorted_list[j] < unsorted_list[j - 1]:
                tmp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j - 1]
                unsorted_list[j - 1] = tmp
                is_sorted = False
        if is_sorted:
            break
    print("sorted list : {}".format(unsorted_list))
    print("sorted number : {}".format(count))


if __name__ == '__main__':
    test_list = [23, 6, 7, 4, 5, 34, 2, 9, 1, 0, 11, 23, 34, 52, 38, 21]
    bubble_sort(test_list)
    test_list = [23, 6, 7, 4, 5, 34, 2, 9, 1, 0, 11, 23, 34, 52, 38, 21]
    bubble_sort_with_mark(test_list)
    test_list = [23, 6, 7, 4, 5, 34, 2, 9, 1, 0, 11, 23, 34, 52, 38, 21]
    bubble_sort_with_boundary(test_list)
    test_list = [23, 6, 7, 4, 5, 34, 2, 9, 1, 0, 11, 23, 34, 52, 38, 21]
    cocktail_sort(test_list)
