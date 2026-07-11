class Solution(object):
    def countBeautifulPairs(self, nums):
        count = 0
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        for i in range(len(nums)):
            first = nums[i]
            while first >= 10:
                first //= 10
            for j in range(i + 1, len(nums)):
                last = nums[j] % 10
                if gcd(first, last) == 1:
                    count += 1
        return count