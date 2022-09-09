class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []                    # ans
        for x in range(1, n + 1):       # go through numbers 1 - n
            
            if x % 3 == 0 and x % 5 == 0:       
                ans.append("FizzBuzz")
            elif x % 3 == 0:
                ans.append("Fizz")
            elif x % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(x))
        return ans                      # return
        