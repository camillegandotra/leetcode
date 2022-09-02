class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:    # if the number is 0 or less than 0 then return False cause it aint a power of 3
            return False
        while n != 1:       # reduce n by n / 3, to make sure it is a power of 3
            if n % 3 != 0:      # if there is a remainder, it aint a power of 3, thus return False
                return False
            n = n / 3     # reduce n by n / 3
        return True       # when we get n == 1, then we know it is a power of 3
        
        