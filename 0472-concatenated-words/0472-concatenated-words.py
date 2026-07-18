class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        words.sort(key=len)
        d = set()
        ans = []
        def can(word):
            if not d:
                return False
            dp = [False] * (len(word) + 1)
            dp[0] = True
            for i in range(1, len(word) + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in d:
                        dp[i] = True
                        break
            return dp[-1]
        for w in words:
            if can(w):
                ans.append(w)
            d.add(w)
        return ans