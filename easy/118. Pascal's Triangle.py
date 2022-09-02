class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []                # store our ans
        before = [1,1]                  # keep track of before array
        for x in range(numRows):            # for the num or rows (input)
            if x == 0:                          # for the first row, it is [1]
                ans.append([1])
            elif x == 1:                        # second row, it is [1,1]
                ans.append([1,1])
                
            else:                                   # if we are working on the other rows, we do this pattern
                temp = [1]                          # first item of the array is always 1
                for z in range(len(before) - 1):            # then go through the before array and append the sum of the one and the next one.
                    temp.append(before[z] + before[z + 1])
                temp.append(1)                  # last one is always 1
                before = temp                   # make this the new before for next iteration
                ans.append(temp)                # append it to ans
                
                
                
        return ans                  # after return ans
            
            
            
        