class Solution(object):
    def findTheDifference(self, s, t):
        st = sorted(s)
        ts = sorted(t)
        for i in range(len(st)):
            if st[i] != ts[i]:
                return ts[i]
        return ts[-1]