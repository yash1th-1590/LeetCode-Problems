class Solution(object):
    def countAndSay(self, n):
        s = "1"
        for _ in range(n - 1):
            t = ""
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                t += str(j - i) + s[i]
                i = j
            s = t
        return s