"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        # Insert deep copies of each node next to ...
        # ... the original node
        n = head
        while n != None:
            # Create new node
            new = Node(n.val)
            new.next = n.next
            n.next = new
            n = n.next.next

        # Fix the random connections to match that of ...
        # ... the original node (to the new node)
        n = head
        while n != None:
            # get the og random node
            # put the copy node (next to og) rnd connection ...
            # ... to the copy random node (next to og.rnd)
            rnd = n.random
            if rnd:
                n.next.random = rnd.next
            else:
                n.next.random = None
            n = n.next.next

        # Pull out the deep copy and fix the next links.
        n = head
        if n:
            ret = head.next
        else:
            ret = None

        while n != None:
            temp = n.next.next  # next og node
            # if we have a next og node that means its next is its copy, else None
            # Fix copy next links
            if n.next.next:       
                n.next.next = n.next.next.next 
            else:
                n.next.next = None
            
            # Fix og next links
            n.next = temp

            # Go to next og node
            n = temp

        # Printing
        # x = ret
        # while x != None:
        #     print("val:")
        #     print(x.val)

        #     print("next:")
        #     if x.next:
        #         print(  x.next.val)
        #     else:
        #         print(" none")
        #     print("rand:")
        #     if x.random:
        #         print(  x.random.val)
        #     else:
        #         print(" none")
        #     x = x.next

        return ret

