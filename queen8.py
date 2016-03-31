#!/usr/bin/env python
#coding=utf-8

# 为保证两个整数相除结果为浮点数。
from __future__ import division
from pprint import pprint

# 定义棋盘。
board = [[0 for x in range(8)] for y in range(8)]

# 用于存放皇后位置。
queens = {}

# 记录解的个数。
total = 0

def check(col,row):
    '''检查(row,col)此位置是否可以放置皇后，row表示行，col表示列'''
    # 如果是第一列，则肯定可以放置皇后，返回True。
    if col == 0: return True

    # 检查已经存在的皇后与当前格子是否在同一行或对角线上。
    # 因为一列只能有一个皇后，所以按列遍历。
    for k in range(col):
        if row == queens[k] or abs((row-queens[k])/(col-k)) == 1:
            return False
    # 循环结束，没有返回，说明该位置不与存在的任一皇后在一条横线或对角线上，可放。
    return True

def start(col):
    for row in range(8):
        if check(col,row):
            # 保存已放置皇后位置。
            queens[col] = row
            # 在棋盘上标记位置，用于打印。
            board[row][col] = 1
            # 如果是最后一列，则放下该位置后打印结果。
            if col == 7:
                # 计算解的个数。
                global total
                total = total + 1
                # 打印棋盘。
                pprint(board)
                # 打印一个空行，用于分隔每个结果。
                print
                # 最后一列可能不只一个位置有解，打印后删掉刚加入的皇后位置，清扫棋盘，接着循环找下一位置。
                del queens[col]
                board[row][col] = 0
                continue
            # 如果不是最后一列，则开始找下一列的皇后。
            else:
                # 如果下一列没有位置可以放置皇后，删掉最新的皇后，接着循环。
                if not start(col + 1):
                    del queens[col]
                    board[row][col] = 0
                    continue

if __name__ == '__main__':
    start(0)
    print '共%d个解' % total

