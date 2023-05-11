class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        sign = 0
        if s[0] == '-':     # check if first index is -
            sign = -1       # sign is -1
            r = s[1::]      # remove neg sign
            r = r[::-1]     # reverse int
        else:
            sign = 1        # num is pos
            r = s[::-1]     # reverse int

        if len(bin(int(r))[2:]) >= 32:  # if exceeds range, return 0
            return 0

        return int(r) * sign        # return int of r * sign


        