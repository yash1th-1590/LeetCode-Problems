class Solution(object):
    def gcdOfOddEvenSums(self, n):
        sumOdd = n*n
        sumEven = n*(n+1)
        while sumEven!=0:
            sumOdd,sumEven=sumEven,sumOdd%sumEven
        return sumOdd