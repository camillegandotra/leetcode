# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        faster = head           # create a faster pointer which we will go by 2.
        
        if not head:            # if empty LL, we return False
            return False
        
        while faster and faster.next:          # basically while we can increment faster by 2
            faster = faster.next.next           # increment faster by 2
            head = head.next                    # increment head by 1
            if head == faster:                  # if they point to same LL, that means there is a loop, which will happen eventually if there is a loop somewhere in the LL
                return True
            
        return False                            # if not, the while loop will break so return False
        