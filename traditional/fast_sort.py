#!/usr/bin/env python
# author: hanwei
# file: fast_sort.py
# time: 2020/10/13 15:33


def fast_sort(num_list, start, end):
    key = num_list[end]
    key_index = start - 1
    if start < end:

        for index in range(start, end):
            if key >= num_list[index]:
                key_index += 1
                num_list[key_index], num_list[index] = num_list[index], num_list[key_index]

        num_list[key_index+1], num_list[end] = num_list[end], num_list[key_index+1]

        fast_sort(num_list, start, key_index-1)
        fast_sort(num_list, key_index+1, len(num_list)-1)

    return num_list


if __name__ == '__main__':
    num_list = [3, 1, 5, 7, 2]
    print(fast_sort(num_list, 0, len(num_list)-1))


