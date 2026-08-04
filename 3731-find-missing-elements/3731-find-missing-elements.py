class Solution(object):
    def findMissingElements(self, nums):
        res = []
        n = len(nums)
        m = min(nums)
        n = max(nums)
        for i in range(m,n+1):
            if i not in nums:
                res.append(i)
        return res