class Solution(object):
    def removeNthFromEnd(self, head, n):

        temp = ListNode(0)
        temp.next = head

        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        curr = temp
        for i in range(length - n):
            curr = curr.next

        curr.next = curr.next.next

        return temp.next