# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:         # base case when we get to NULL Nodes, we make sure both are NULL, then return True because the rest in the path is fine if it gets to this point    
            return True
        
        if (p and not q) or (q and not p):             # if one and not the other, obvi return False
            return False
        
        if p and q and p.val != q.val:                 # if we have nodes of both, check their vals , if thhey dont equal then obvi return false, if they do equal, continue
            return False
        
    
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)        # return the recursive function for the left and right side of the head.
        