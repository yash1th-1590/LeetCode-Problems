class Solution:
    def shortestBeautifulSubstring(self, s, k):
        n = len(s)
        best = ""
        min_len = float('inf')
        for i in range(n):
            count = 0
            for j in range(i, n):
                if s[j] == '1':
                    count += 1
                if count == k:
                    current = s[i:j + 1]
                    if len(current) < min_len:
                        min_len = len(current)
                        best = current
                    elif len(current) == min_len:
                        best = min(best, current)
                    break
        return best