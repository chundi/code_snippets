class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        l = len(s)
        if l <= 1:
            return True
        i = 0
        j = l - 1
        while True:
            _p = ''
            _s = ''
            while True:
                if i == l:
                    return True
                if s[i].isalnum():
                    _p = s[i].lower()
                i = i + 1
                if _p:
                    break
            while True:
                if s[j].isalnum():
                    _s = s[j].lower()
                j = j - 1
                if _s:
                    break
            if _p != _s:
                return False
            if i >= j:
                return True

