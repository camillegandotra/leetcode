class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)      # Counter() gets us a dictionary with each characters to the number of times it is in s
        
        for x in range(len(s)):     # go through all the indexs of s
            if count[s[x]] == 1:        # if the char at that index has a value == 1 in count, return the index (because it is the first occurance of it)
                return x
        return -1           # if we go through all the char in s and no unique char, return -1
        