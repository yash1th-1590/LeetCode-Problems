class Solution(object):
    def findRestaurant(self, list1, list2):
        d = {}
        for i in range(len(list1)):
            d[list1[i]] = i
        ans = []
        mini = float('inf')
        for j in range(len(list2)):
            if list2[j] in d:
                s = d[list2[j]] + j
                if s < mini:
                    mini = s
                    ans = [list2[j]]
                elif s == mini:
                    ans.append(list2[j])

        return ans