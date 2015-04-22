class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0: return [1,]
        m = lambda i:reduce(lambda x,y: x*y, xrange(1, i + 1))
        a = [1, ]
        l = rowIndex/2
        i = 1
        up = m(rowIndex)
        while i <= l:
            a.append(up/(m(i)*m(rowIndex-i)))
            i = i + 1
        if rowIndex % 2 == 0:
            a.extend((a[:-1])[::-1])
        else:
            a.extend(a[::-1])
        return a

