class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next
        index = 1
        first = -1
        last = -1
        minDist = 1000000
        while curr.next:
            nxt = curr.next
            if (curr.val > prev.val and curr.val > nxt.val) or \
               (curr.val < prev.val and curr.val < nxt.val):
                if first == -1:
                    first = index
                else:
                    minDist = min(minDist, index - last)
                last = index
            prev = curr
            curr = nxt
            index += 1
        if first == last:
            return [-1, -1]
        maxDist = last - first
        return [minDist, maxDist]
        