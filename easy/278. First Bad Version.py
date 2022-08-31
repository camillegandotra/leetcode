# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1      # initial values
        end = n
        
        while start <= end:    # so we never get start > end
            
            if isBadVersion(start):             # check if start is bad, if yes, return start
                return(start)
            
            mid = (start + end) // 2            # find middle
            
            checker = isBadVersion(mid)         # check if middle is bad
                
            if checker:                         # if yes, we change end to be mid (including it cause it might be the first one)
                end = mid 
                continue                        # continue to next iteration
                
            if not checker:                     # if no, we change start to be mid + 1, cause we know mid aint the first one
                start = mid + 1
                    
        return end                              # after everything, we return end because start and mid isnt so.
                
        