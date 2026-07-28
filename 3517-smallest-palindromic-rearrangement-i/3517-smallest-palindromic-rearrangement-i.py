class Solution(object):
    def smallestPalindrome(self, s):
        f = [0] * 26
        for ch in s:
            f[ord(ch) - ord('a')] += 1
        left = []
        middle = ""
        for i in range(26):
            left.append(chr(i + ord('a')) * (f[i] // 2))
            if f[i] % 2:
                middle = chr(i + ord('a'))
        left = ''.join(left)
        return left + middle + left[::-1]
        