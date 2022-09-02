class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = []           # records previous nums, so if it is a repeat, we know its a cycle, so we return False
        
        while True:         # forever loop
            if n in nums:           # if the number is in nums, return False
                return False
            else:                   # else, we append it to the list nums
                nums.append(n)  
            temp = 0                # to hold the sum of the square of each digit in the num
            for x in str(n):                # iterate through each digit (done by making num a str)
                temp += (int(x) * int(x))       # square and add to temp
            if temp == 1:                       # if we get 1, great, return True
                return True
            n = temp                            # if not, temp is our new num, go again
            
                
                
        