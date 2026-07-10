class Solution(object):
    def majorityElement(self, nums):
        n = None
        count = 0
        for num in nums:
            if count == 0:
                n = num
                count = 1
            elif num == n:
                count += 1
            else:
                count -= 1
        
        return n