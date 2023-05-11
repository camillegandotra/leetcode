# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (head != None and head.next != None):    # checks if LL is not nothing and not just one node
            # reduce number of k's to minimum
            # loop through once, get length of LL
            l = 1
            cur = head
            cur_prev = None
            while cur.next != None:
                l += 1
                cur_prev = cur
                cur = cur.next
            if (k > l):
                    k = k % l
            
            # rotate k by the minimum k times
            while k > 0:
                l = 1
                cur = head
                cur_prev = None
                while cur.next != None:     # get to end of LL
                    l += 1
                    cur_prev = cur
                    cur = cur.next
                cur.next = head
                head = cur
                cur_prev.next = None
                k -= 1

        return head # return LL
                