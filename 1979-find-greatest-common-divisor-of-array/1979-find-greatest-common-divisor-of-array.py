class Solution(object):
    def findGCD(self, nums):
        from collections import Counter
        a = min(nums)
        b = max(nums)
        while b:
            a, b = b, a % b
        return a

        