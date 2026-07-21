class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        ones = s.count('1')
        s = "1" + s + "1"
        runs = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            i = j
        g = 0
        for i in range(1, len(runs) - 1):
            if runs[i][0] == '1' and runs[i - 1][0] == '0' and runs[i + 1][0] == '0':
                g = max(g, runs[i - 1][1] + runs[i + 1][1])
        return ones + g
        