class Solution(object):
    def moveZeroes(self, nums):
        for x in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
