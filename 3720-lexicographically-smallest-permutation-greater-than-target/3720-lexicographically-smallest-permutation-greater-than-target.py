class Solution(object):
    def lexGreaterPermutation(self, s, target):
        base = [0] * 26

        for ch in s:
            base[ord(ch) - 97] += 1

        n = len(s)

        for i in range(n - 1, -1, -1):
            cnt = base[:]
            possible = True

            for j in range(i):
                x = ord(target[j]) - 97
                cnt[x] -= 1
                if cnt[x] < 0:
                    possible = False
                    break

            if not possible:
                continue

            x = ord(target[i]) - 97

            for c in range(x + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1

                    ans = target[:i] + chr(c + 97)

                    for j in range(26):
                        ans += chr(j + 97) * cnt[j]

                    return ans

        return ""