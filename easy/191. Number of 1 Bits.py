class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:       # while n is not all 0s
            if n & 1:       # checks last digit in n
                count += 1      # if 1, increase count
            n = n >> 1          # shift right by 1
        return count            # return counnt
            
    