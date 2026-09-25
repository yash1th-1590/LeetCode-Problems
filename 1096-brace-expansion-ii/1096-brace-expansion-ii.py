class Solution:
    def braceExpansionII(self, expression):
        def solve(s):
            if not s:
                return [""]

            if s[0] == '{':
                level = 0
                end = 0

                for i in range(len(s)):
                    if s[i] == '{':
                        level += 1
                    elif s[i] == '}':
                        level -= 1
                        if level == 0:
                            end = i
                            break

                parts = []
                start = 1
                level = 0

                for i in range(1, end):
                    if s[i] == '{':
                        level += 1
                    elif s[i] == '}':
                        level -= 1
                    elif s[i] == ',' and level == 0:
                        parts.append(s[start:i])
                        start = i + 1

                parts.append(s[start:end])

                left = []

                for p in parts:
                    left += solve(p)

                right = solve(s[end + 1:])

                return [a + b for a in left for b in right]

            left = [s[0]]
            right = solve(s[1:])

            return [a + b for a in left for b in right]

        return sorted(set(solve(expression)))