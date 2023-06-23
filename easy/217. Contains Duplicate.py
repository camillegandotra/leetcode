class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # This means every number is there once...thus return False
        if len(nums) == len(set(nums)):
            return False
        else:
            return True

        # Other Solution
        
        # seen = set()
        # for x in nums:
        #     if x in seen:
        #         return True
        #     else:
        #         seen.add(x)
        # return False
        