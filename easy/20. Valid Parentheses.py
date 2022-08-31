class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        key = { '(' : ')', '[' : ']', '{' : '}'}        #dictionary with open to close
        check = []                                      #list used as stack FILO (first in last out)
  
        for x in s:                                     #go throu all x in s
            if x in key.keys():                         #if x is an opener, add the corresponding closer to the stack
                check.append(key[x])
                continue
            if x in check:                              #else x has to be a closer, first check if it even is in our stack, if not, return False
                o = check.pop()                         #now pop the stack (get the last entry to the stack)
                if x == o:                              #if x is that last entry, continue, because it is valid
                    continue                    
            return False                                #if x is not the last entry, return False, because it is not valid
        
        if len(check) == 0:                             #check is our stack is empty after all iterations, because thats what makes it valid
            return True
        return False

                
            
                

            
    
        