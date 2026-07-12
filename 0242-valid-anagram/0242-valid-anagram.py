class Solution(object):
    def isAnagram(self, s, t):
        st = sorted(s)
        ts = sorted(t)
        return st == ts