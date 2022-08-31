class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        maglist = list(magazine)     # made them lists for conv
        
        
        for x in list(ransomNote):      # go through each char in ransomNote
            if x in maglist:                # if x is in maglist, cool, remove it and go to next
                maglist.remove(x)
            else:
                return False                # else, then ransomNote cant be contructed using magazine so return False
        
        return True             # if we eventually never return False, then return True
   

        