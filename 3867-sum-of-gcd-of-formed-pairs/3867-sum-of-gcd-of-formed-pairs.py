class Solution(object):
    def gcdSum(self, nums):
        n = len(nums)
        prefixGcd = []
        mx = 0
        for num in nums:
            if num > mx:
                mx = num
            a, b = num, mx
            while b:
                a, b = b, a % b
            prefixGcd.append(a)
        prefixGcd.sort()
        ans = 0
        l, r = 0, n - 1
        while l < r:
            a, b = prefixGcd[l], prefixGcd[r]
            while b:
                a, b = b, a % b
            ans += a
            l += 1
            r -= 1
        return ans