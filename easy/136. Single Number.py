class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        
        tracker = dict()            # empty dict to act as counter 
        dup = []                    # list to store duplicates
        
        for x in nums:              # go through each number in nums
            try:
                tracker[x] += 1         # if it is a duplicate it will go through try, so we append it to dup
                dup.append(x)   
            except:                    # if it is not a duplicate, we make the counter = 1
                tracker[x] = 1
                
        return list(set(nums) - set(dup)).pop()             # use set to get the only remanding one, return
    
        '''
        counter = Counter(nums)                 # same thing, Counter basically acts as a counter, so we return the key in the dictionary whose value is 1
        for x,y in counter.items():
            if y == 1:
                return x
        '''
                
            
        