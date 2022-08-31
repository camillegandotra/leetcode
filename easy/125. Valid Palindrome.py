class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = (''.join(c for c in s if c.isalpha() or c.isdigit())).lower()   #makes s without spaces, and only has a-z and digits

        if s == s[::-1]:                                       #check if s == s's reverse
            return True                                        #if yes then it is True (it is a valid palindrome)
        return False                                           # else, it is not valid; False
        
        