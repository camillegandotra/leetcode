class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # writing a binary search algorithm which has o(log n) runtime copmplexity
            # aka we cant just use python index stuff to locate where the target is in the list
        
        
        low = 0                         # beginning low is 0 index      
        high = len(nums) - 1            #beginning high is the last index
        
        
        while low <= high:      #while loop (eventually the middle will be the target if it exists)
            
            mid = (low + high) // 2          # find the mid index of list
            
            if nums[mid] == target:         # if the mid is the target, great return mid index
                return mid

            elif target < nums[mid]:            # if target is less than the number at mid index, we change range of list by focusing to the left of mid
                high = mid - 1                  # hence we make the high one less than mid (cause we already looked at mid)
                   
            elif target > nums[mid]:            # if target is more than the number at mid index, we change range of list by focusing to the right of mid
                low = mid + 1                   # hence we make the low one more than mid (cause we already looked at mid)
                

        return -1                    # if target not in  nums we return -1
        
        
        
        
        
        