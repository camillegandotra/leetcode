# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Return Node
        res = ListNode()

        # 2 pointer
        one = res
        one.next = head
        two = head

        # Iterate one pointer n - 1 times (since first pointer is 1 before head)
        for x in range(n - 1):
            two = two.next

        # Go till two is at the end of LL
        while two.next != None:
            two = two.next
            one = one.next
        
        # Remove node after one
        one.next = one.next.next

        # Return res.next
        return res.next
        