class Solution(object):
    def mySqrt(self, x):
        
        if x < 2:
            return x
        
        left, right = 0, x
        
        while left <= right:
            mid = (left + right) // 2
            sqr = mid * mid
            
            if sqr == x:
                return mid
            elif sqr < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right