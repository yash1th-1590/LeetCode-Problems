class Solution(object):
    def sumGame(self, num):
        n = len(num)
        half = n // 2
        diff = 0
        left_q = 0
        right_q = 0
        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                diff += int(num[i])
        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                diff -= int(num[i])
        if (left_q + right_q) % 2:
            return True
        return diff != 9 * (right_q - left_q) // 2