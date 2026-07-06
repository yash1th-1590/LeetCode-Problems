class Solution(object):
    def missingNumber(self, nums):
        size = len(nums)
        for i in range(size+1):
            if i not in nums:
                return i
        