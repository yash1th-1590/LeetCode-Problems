class Solution(object):
    def maxNumberOfBalloons(self, text):
        times = {}
        for ch in text:
            times[ch] = times.get(ch, 0) + 1
        return min(
            times.get('b', 0),
            times.get('a', 0),
            times.get('l', 0) // 2,
            times.get('o', 0) // 2,
            times.get('n', 0)
        )
        