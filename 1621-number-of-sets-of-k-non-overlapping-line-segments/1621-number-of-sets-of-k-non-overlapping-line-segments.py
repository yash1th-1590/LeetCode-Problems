class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7
        dp = [[0] * (2 * k + 1) for _ in range(n + k)]

        dp[0][0] = 1

        for i in range(1, n + k):
            for j in range(2 * k + 1):
                dp[i][j] = dp[i - 1][j]
                if j:
                    dp[i][j] += dp[i - 1][j - 1]
                dp[i][j] %= MOD

        return dp[n + k - 1][2 * k]
        