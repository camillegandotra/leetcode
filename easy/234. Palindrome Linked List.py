# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """   
        check = []
        while head:                     # go through the LL, record each val in check
            check.append(head.val)
            head = head.next
        
        x = 0
        y = len(check) - 1
        
        while x < y:                    # check first and last, keep going till mid, compare each val, make sure they are equal.
            if check[x] == check[y]:
                x += 1
                y -= 1
                continue
            else:
                return False

            
        return True
 
        
        