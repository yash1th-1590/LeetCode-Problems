class Solution(object):
    def gcdValues(self, nums, queries):
        m = max(nums)
        f = [0] * (m + 1)
        for x in nums:
            f[x] += 1
        c = [0] * (m + 1)
        for i in range(1, m + 1):
            j = i
            while j <= m:
                c[i] += f[j]
                j += i
        g = [0] * (m + 1)
        for i in range(m, 0, -1):
            g[i] = c[i] * (c[i] - 1) // 2
            j = i * 2
            while j <= m:
                g[i] -= g[j]
                j += i
        p = [0] * (m + 1)
        for i in range(1, m + 1):
            p[i] = p[i - 1] + g[i]
        ans = []
        for q in queries:
            l, r = 1, m
            while l < r:
                mid = (l + r) // 2
                if p[mid] > q:
                    r = mid
                else:
                    l = mid + 1
            ans.append(l)
        return ans