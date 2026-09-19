class Solution(object):
    def primePalindrome(self, n):
        def is_prime(num):
            if num < 2:
                return False
            if num % 2 == 0:
                return num == 2
            i = 3
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 2
            return True
        if 8 <= n <= 11:
            return 11
        length = len(str(n))
        while True:
            half_len = (length + 1) // 2
            start = 10 ** (half_len - 1)
            end = 10 ** half_len
            for half in range(start, end):
                s = str(half)
                palindrome = int(s + s[-2::-1])
                if palindrome >= n and is_prime(palindrome):
                    return palindrome
            length += 1