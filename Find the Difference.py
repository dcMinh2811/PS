class Solution(object):
    def findTheDifference(self, s, t):
        s = sorted(s)
        t = sorted(t)
        index = 0
        while True:
            try:
                if s[index] == t[index]:
                    index += 1
                else:
                    return t[index]
                    break
            except IndexError:
                return t[index]
                break
