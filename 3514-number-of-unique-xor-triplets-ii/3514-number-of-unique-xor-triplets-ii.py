class Solution(object):
    def uniqueXorTriplets(self, nums):
        nums = list(set(nums))
        p = set()
        for a in nums:
            for b in nums:
                p.add(a ^ b)
        res = set()
        for x in p:
            for c in nums:
                res.add(x ^ c)
        return len(res)