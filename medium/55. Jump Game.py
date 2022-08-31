class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = len(nums)-1      # get the last index in nums 
        for i in range(len(nums)-2,-1,-1): # Iterate backwards from second to last item until the first item
            if (i + nums[i]) >= last: # If this index has jump count which can reach to or beyond the last position then we want to make it the new last
                last = i # Since we just need to reach to this new index
        return last == 0	# if it is 0, that means it is possible, if not, then not possible. 
        
        
        
        '''                     # too slow
        first = nums.pop(0)
        
        if first == 0 and len(nums) != 0:
            return
        
        print(nums)
        
        if len(nums) == 0:
            print('empty, solution found')
            return True
        

        
      
        
        for x in range(first - 1, -1, -1):
            try:
                if self.canJump(nums[x:]):
                    return True
            except:
                continue

            
        return False

        '''
            
            
            
        