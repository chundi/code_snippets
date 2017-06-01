# -*- coding:utf-8 -*-

def binary_search(li, x):
    start = 0
    end = len(li) - 1
    while start <= end:
        idx = (start + end) / 2
        if x > li[idx]:
            start = idx + 1
        elif x < li[idx]:
            end = idx - 1
        else:
            return idx
    return -1

