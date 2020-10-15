#!/usr/bin/env python
# author: hanwei
# file: two_sum.py
# time: 2020/10/15 09:52


def two_sum(num_list, target):

    result_list = []
    for index, num in enumerate(num_list):
        other_num = target - num
        if other_num in num_list[index+1:]:
            result_list.append(index)
            result_list.append(num_list.index(other_num, index))
            return result_list
    return result_list


if __name__ == '__main__':
    num_list = [1, 3, 2, 6, 8]
    target = 9
    print(two_sum(num_list, target))

