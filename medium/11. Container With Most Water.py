class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0                    # left pointer at first index
        right = len(height) - 1         # right pointer at last index
        max_area = 0                    # initialize max area to return to zero 
        
        while left < right:             # while we are comparing 
            temp_area = min(height[right], height[left]) * (right - left)       # get the area
            
            if temp_area > max_area:            # if this area is bigger, store it
                max_area = temp_area
            
            
            if height[right] < height[left]:            # whatever one is shorter, we want to increment in hopes of getting a taller one
                right -= 1
            
            else:
                left += 1
        
        return max_area             # return max_area
        
        
        
    
        '''
        
        max_area = 0
        
        
        
        for x in range(len(height)):
            for y in range(len(height)):
                if x < y:
                    if ((abs(y - x)) * min(height[x],height[y])) > max_area:
                        max_area = ((abs(y - x)) * min(height[x],height[y]))
                else:
                    continue
                        
        return max_area
        
        '''
        