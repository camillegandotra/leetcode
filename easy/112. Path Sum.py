# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
 
        temp = 0                        # stores cur sum at cur node
        
        def dfs(root, temp, targetSum):     # recursive function (DFS); this function will boil down to a leaf node, which we will return True or False, if the temp_sum == targetSum
                
            if not root:                    # if not root, we return False
                return False
            
            temp += root.val                # increase temp_sum
            
          
            if not root.left and not root.right:        # if we are at a leaf node, check condition (return True or False)
                return targetSum == temp
            
            return dfs(root.left, temp, targetSum) or dfs(root.right, temp, targetSum)      # if not leaf, keep searching till we get to leaf, here we return True or False, it will return True if at least one path has temp_sum == targetSum
        
        return dfs(root, temp, targetSum)               # return the function to call it
            