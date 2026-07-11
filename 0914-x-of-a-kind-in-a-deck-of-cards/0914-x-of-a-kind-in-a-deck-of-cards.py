class Solution(object):
    def hasGroupsSizeX(self, deck):
        from collections import Counter
        freq = Counter(deck)
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        g = 0
        for count in freq.values():
            g = gcd(g, count)
        return g >= 2