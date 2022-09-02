class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        

        return str(x) == str(x)[::-1]   # turn int -> str, return True if it is equal to the reverse, else False
        