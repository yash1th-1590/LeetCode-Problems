class Solution(object):
    def modifyString(self, s):
        s = list(s)
        n = len(s)
        for i in range(n):
            if s[i] == '?':
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if (i > 0 and s[i - 1] == ch):
                        continue
                    if (i < n - 1 and s[i + 1] == ch):
                        continue
                    s[i] = ch
                    break
        return "".join(s)