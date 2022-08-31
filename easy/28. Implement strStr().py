class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        return haystack.find(needle)        # find string method returns the starting index of needle in haystack
    
    '''
        if needle in haystack:                  # same thing lolz
            return haystack.index(needle)
            
        return -1
    '''