class Solution(object):
    def lengthOfLastWord(self, s):
        list1 = s.split()
        return len(list1[-1])
        