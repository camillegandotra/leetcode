class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
  
        return len(s.split().pop())  # split method on a string, makes it into a list with just the words, take the last item with .pop and return lenght
        