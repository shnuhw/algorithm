#!/usr/bin/env python
# author: hanwei
# file: binary_search.py
# time: 2020/10/13 11:10


def binary_search(num_list, key):
    """
    递归二分查找
    :param num_list: 已经排序好的列表
    :param key: 需要查询的数字
    :return: 是否在list中
    """

    start = 0
    end = len(num_list) - 1
    mid = len(num_list) // 2
    if start > end:
        return False
    if start == end:
        if num_list[0] == key:
            return True
        return False
    if key == num_list[mid]:
        return True
    if key < num_list[mid]:
        num_list_left = num_list[start:mid]
        return binary_search(num_list_left, key)
    else:
        num_list_right = num_list[mid:]
        return binary_search(num_list_right, key)


def binary_search_loop(num_list, key):
    """
    非递归二分查找
    :param num_list: 已经排序好的列表
    :param key: 需要查询的数字
    :return: 是否在list中
    """
    start = 0
    end = len(num_list) - 1
    mid = len(num_list) // 2

    while start < end:

        if key == num_list[mid]:
            return True
        if key < num_list[mid]:
            num_list = num_list[start:mid]
        else:
            num_list = num_list[mid:]

        start = 0
        end = len(num_list) - 1
        mid = len(num_list) // 2

    return False


if __name__ == '__main__':
    import random
    key1 = random.randint(-5, 9)
    key2 = random.randint(-5, 9)
    search_list = [1, 2, 3, 4, 5]
    print(key1, binary_search(search_list, key1))
    print(key2, binary_search_loop(search_list, key2))

