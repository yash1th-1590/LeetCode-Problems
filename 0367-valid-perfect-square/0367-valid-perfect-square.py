class Solution(object):
    def isPerfectSquare(self, num):
        root = int(num**0.5)
        return root*root == num