# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        temp_node = ListNode()             #temp_node and cur_node are the same ListNode() object; temp_node points at the node before our head
        cur_node = temp_node                #while we use cur_node to traverse our new ListNode() object
        
        while list1 and list2:              #while list1 and list2 have nodes in their list
            if list1.val < list2.val:         #look at the current value, if list1 is lower:
                cur_node.next = list1           #we add list1 to the next node of cur_node
                list1 = list1.next              #update list1 to its next node
            else:                             #else list2 is lower or equal:
                cur_node.next = list2           #we add list2 to the next node of cur_node
                list2 = list2.next              #update list2 to its next node      
            
            cur_node = cur_node.next        #update cur_node to its next node
        
        if list1:                          #if there is no more list2, we just append list1 to the next node of cur_node
            cur_node.next = list1
            
        
        if list2:                           #if there is no more list1, we just append list2 to the next node of cur_node
            cur_node.next = list2           
                
        
        return temp_node.next               #we return temp_node.next because that points to th head of our new LL object
        
        
            