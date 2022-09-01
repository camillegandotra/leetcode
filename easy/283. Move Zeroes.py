class Solution(object):
    def moveZeroes(self, nums):
        
        non_zero_index = 0           # tracker to see where the non_zero items need to be placed (in order) to modify the list
        
        for x in range(len(nums)):          # go through all the indexs of nums
            if nums[x] != 0:                        # if the item at that index does not equal 0, we need to place it where it belongs
                nums[non_zero_index] = nums[x]      # use the non_zero_index to place that item in order
                non_zero_index += 1                 # then += 1, to get ready for next index
                
                
                # this is done to get rid of all 0s in the array ( in the front part)
                
        for x in range(non_zero_index, len(nums)):          # after we handled all the nums we care about, then for the remainding space in nums, we fill them with 0
            nums[x] = 0
            
        
            
        return nums
        
                    
        """                     # changes size of nums so we cant do that.
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        if len(nums) == 1 or len(nums) == 0:
            return nums
        
        double_zeros =
        
        x = 0
        y = 1
        
        while y < len(nums):
            if nums[x] = 0 and nums[x] < nums[y]:
                temp = nums[x]
                nums[x] = nums[y]
                nums[y] = temp
                
            elif 0 = nums[x] = nums[y]:
                
                
            y += 1
            x += 1
                
        '''
        