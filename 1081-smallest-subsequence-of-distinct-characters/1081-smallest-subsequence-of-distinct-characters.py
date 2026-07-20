class Solution(object):
    def smallestSubsequence(self, s):
        from collections import Counter
        
    
        count = Counter(s)
        stack = []
        in_stack = set()
        
        for char in s:
            count[char] -= 1
            
            if char in in_stack:
                continue
                
            while stack and char < stack[-1] and count[stack[-1]] > 0:
                in_stack.remove(stack.pop())
            
            stack.append(char)
            in_stack.add(char)
        
        return ''.join(stack)
        