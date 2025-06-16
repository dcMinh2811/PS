class Solution(object):
    def plusOne(self, digits):
        num = ""
        for n in digits:
            num += str(n)
        num = str(int(num) + 1)
        l = []
        for n in num:
            l.append(int(n))
        return l
