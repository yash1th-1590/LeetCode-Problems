class Solution(object):
    def thirdMax(self, nums):
        a = b = c = float("-inf")
        s = set()
        for x in nums:
            if x in s:
                continue
            s.add(x)
            if x > a:
                a, b, c = x, a, b
            elif x > b:
                b, c = x, b
            elif x > c:
                c = x
        return c if len(s) >= 3 else a