class Solution(object):
    def arraySign(self, nums):
        x = 1
        for n in nums:
            x *= n
        if x > 0:
            return 1
        elif x == 0:
            return 0
        else:
            return -1
