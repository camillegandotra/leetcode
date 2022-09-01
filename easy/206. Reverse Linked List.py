# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        prev = None       # initialize the first prev to None (because we at the head)
        cur = head        # cur is head 
        
        while cur:              # while we have nodes left
            tmp = cur.next          # this is the rest of the LL to store
            cur.next = prev         # cur.next is now None, 
            prev = cur              # make prev now cur
            cur = tmp               # cur is now rest of LL

                
        return prev         # return prev
        
        
        '''
        newLL = ListNode()
        newCurNode = newLL
        
        tail = head
        
        if not head or not head.next:
            return head
        
        
        while True:
            tail = tail.next
            if tail.next == None:
                newCurNode.next = tail
                newCurNode = newCurNode.next
                print(newCurNode.val)
                break
                
        traverser = head
        
        while True:
            if traverser.next == newCurNode:
                newCurNode.next = traverser
                newCurNode = newCurNode.next
                print(newCurNode.val)
                traverser = head
                continue
            traverser = traverser.next
            if newCurNode == head:
                newCurNode.next = None
                break
        
        return newLL.next
            
            
                
        '''
        
        
        