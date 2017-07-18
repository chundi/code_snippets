# -*- coding:utf-8 -*-

'''
question: https://leetcode.com/problems/search-a-2d-matrix/
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        sline = 0
        eline = len(matrix) - 1
        while sline <= eline:
            mline = (sline + eline) / 2
            line = matrix[mline]
            if not line:
                sline = mline + 1
                continue
            if line[-1] < target:
                sline = mline + 1
            elif line[0] > target:
                eline = mline - 1
            else:
                s = 0
                e = len(line) - 1
                while s <= e:
                    m = (s + e) / 2
                    if line[m] > target:
                        e = m - 1
                    elif line[m] < target:
                        s = m + 1
                    else:
                        return True
                return False
        return False
