class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n <= 0:    # if the number is 0 or less than 0 then return False cause it aint a power of 2
            return False
        while n != 1:       # reduce n by n / 2, to make sure it is a power of 2
            if n % 2 != 0:      # if there is a remainder, it aint a power of 2, thus return False
                return False
            n = n / 2     # reduce n by n / 2
        return True       # when we get n == 1, then we know it is a power of 2
        