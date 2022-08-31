class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''                                 # set the prefix to empty string (so if there is no common prefix, we return an empty string, else we build up the prefix with this)
        
        shortest_word_len = len(strs[0])            # first we get the shortest string length in the list, this is basically the max length the prefix can be so we only care about this bound
        
        for x in range(len(strs)):
            if strs[x] != strs[0]:
                if len(strs[x]) < shortest_word_len:
                    shortest_word_len = len(strs[x])
        
        
        
        for x in range(shortest_word_len):      # go through x indexes
            cur = set()                            # create a new set for index x
            for y in strs:                          # go through all the strings in strs, add the character at index x to the
                cur.add(y[x])
            if len(cur) == 1:                       # after that check if the length of the set is equal to 1, if it is that means they have the same character, so we append it to our prefix string
                prefix += list(cur).pop()
            else:                                   # if not they differ, so break the loop
                break
                                
        return prefix                   # return prefix
            
        
                
        