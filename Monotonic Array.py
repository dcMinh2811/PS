class Solution(object):
    def isMonotonic(self, nums):
        inc = False
        dec = False
        for i, n in enumerate(nums):
            try:
                if n > nums[i+1]:
                    dec = True
                elif n < nums[i+1]:
                    inc = True
            except IndexError:
                pass
        if not inc == dec == True:
            return True
        else:
            return False
