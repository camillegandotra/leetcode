class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in range(len(nums) + 1):          # go through the numbers through [0, n + 1 )
            if x not in nums:                   # if it is not in the list, return it cause its the only one not in list.
                return x        
        