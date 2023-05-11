class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        r = []
        for x in nums2:             # go through x in nums2
            if x in nums1:          # if it is in nums1
                nums1.remove(x)     # remove from nums1 to avoid dups
                r.append(x)         # append x to r
    
        return r