class Solution(object):
    def resultArray(self, nums, k):
        n = len(nums)
        ans = [0] * k
        dp = [0] * k
        for num in nums:
            r = num % k
            new_dp = [0] * k
            new_dp[r] += 1
            for x in range(k):
                new_dp[(x * r) % k] += dp[x]
            dp = new_dp
            for x in range(k):
                ans[x] += dp[x]
        return ans
        