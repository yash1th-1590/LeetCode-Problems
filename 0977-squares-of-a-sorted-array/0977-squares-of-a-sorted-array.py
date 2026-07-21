class Solution(object):
    def sortedSquares(self, nums):
        res = []
        for num in nums:
            res.append(num*num)
        return sorted(res)
        