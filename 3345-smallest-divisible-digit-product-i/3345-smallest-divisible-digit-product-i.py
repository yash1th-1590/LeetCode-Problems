class Solution(object):
    def smallestNumber(self, n, t):
        num = n
        while True:
            x = num
            product = 1
            while x > 0:
                digit = x % 10
                product *= digit
                x //= 10
            if product % t == 0:
                return num
            num += 1
        