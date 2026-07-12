class Solution(object):
    def arrayRankTransform(self, arr):
        unique = sorted(set(arr))
        rank = {}
        for i, num in enumerate(unique):
            rank[num] = i + 1
        return [rank[num] for num in arr]