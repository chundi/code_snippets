# -*- coding:utf-8 -*-

def qsort1(li, start, end):
    '''递归原址快排'''
    if start >= end:
        return;
    s = start
    e = end
    while s < e:
        while s < e and li[s] < li[e]:
            s = s + 1
        li[s], li[e] = li[e], li[s]
        while s < e and li[s] <= li[e]:
            e = e - 1
        li[s], li[e] = li[e], li[s]
    qsort1(li, start, s - 1)
    qsort1(li, e + 1, end)

def qsort2(li):
    '''递归非原址快排'''
    if len(li) <= 1:
        return li
    l = [x for x in li[1:] if x <= li[0]]
    r = [x for x in li[1:] if x > li[0]]
    return qsort2(l) + [li[0]] + qsort2(r)

def qsort3(li):
    '''递归非原址三分快排'''
    if len(li) <= 1:
        return li
    l = []
    r = []
    m = [li[0]]
    for x in li[1:]:
        if x < li[0]:
            l.append(x)
        elif x > li[0]:
            r.append(x)
        else:
            m.append(x)
    return qsort3(l) + m + qsort3(r)

def qsort4(li, start, end):
    '''递归原址三分快排'''
    if start >= end:
        return
    s = start
    e = end
    i = s + 1
    while i <= e:
        if li[i] < li[s]:
            li[i], li[s] = li[s], li[i]
            s = s + 1
            i = i + 1
        elif li[i] > li[s]:
            li[i], li[e] = li[e], li[i]
            e = e - 1
        else:
            i = i + 1
    qsort4(li, start, s - 1)
    qsort4(li, e + 1, end)


if __name__ == '__main__':
    from random import randint
    print('-' * 40)
    a = [randint(1, 100) for i in range(10)]
    print('before sort', a)
    qsort1(a, 0, len(a)-1)
    print('qsort1', a)
    print('-' * 40)
    a = [randint(1, 100) for i in range(10)]
    print('before sort', a)
    a = qsort2(a)
    print('qsort2', a)
    print('-' * 40)
    a = [randint(1, 100) for i in range(10)]
    print('before sort', a)
    a = qsort3(a)
    print('qsort3', a)
    print('-' * 40)
    a = [randint(1, 100) for i in range(10)]
    print('before sort', a)
    qsort4(a, 0, len(a) - 1)
    print('qsort4', a)
    print('-' * 40)
