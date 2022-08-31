class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
      
       
        if len(s) != len(t) or len(s) == 0:  #check if the length of s and t are the same, they have to be for it to be true
            return False                     #if len(s) = 0, we cant arrange t to be s can we so. return False
        
        s = list(s)                          #make list of s and t (dont think we have to but makes it easier)
        t = list(t) 
                        
        for x in t:                          #go through all letters in t, if it is in s, we remove it from list(s)
            if x in s:
                s.remove(x)
            else:
                return False                # if its not there, it cant be an anagram so return False
        if len(s) == 0:                     # check if len(s) = 0 after, if it does, return True
            return True
        return False
         