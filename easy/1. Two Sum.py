class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        comMap = dict()   #dictionary that stores all the compliment of the numbers in nums and their index in the list nums
        
        
        
        for i in range(len(nums)): #go through all the numbers in nums
            num = nums[i]
            com = target - num     #go through all the numbers in nums
            
            if num in comMap:               #if num is in comMap, that means that nums compliment exists at nums value pair
                return [comMap[num], i]      #so we return the index value pair of num because num is the complement of another num in nums, and the index i of num
            else:
                comMap[com] = i             # if num is not in comMap, then add the compliment of num with its index to the dictionary
                
      
        
    