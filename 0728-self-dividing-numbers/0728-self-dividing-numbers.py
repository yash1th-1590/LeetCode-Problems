class Solution(object):
    def selfDividingNumbers(self, left, right):
        ans = []
        for num in range(left, right + 1):
            original = num
            temp = num
            valid = True
            while temp > 0:
                digit = temp % 10
                if digit == 0 or original % digit != 0:
                    valid = False
                    break
                temp //= 10
            if valid:
                ans.append(original)
        return ans