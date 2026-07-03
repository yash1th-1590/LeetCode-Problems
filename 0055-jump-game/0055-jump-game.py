class Solution(object):
    def canJump(self, nums):
        farthest = 0
        
        for i, jump in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + jump)
        
        return farthest >= len(nums) - 1