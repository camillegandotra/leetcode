class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0                     # get initial low (index 0)
        high = len(nums) - 1        # get initial high (index len(nums) - 1)
        
        
        while True:                          # forever loop
            mid = (high + low) // 2             # get the mid index
            if nums[mid] == target:             # if nums[mid] == our target, great, return mid (the index)
                return mid  
            if nums[mid] > target:              # if the target is less than the value at mid, make high = mid - 1
                high = mid - 1
                if low == mid:                  # if we get at the case where low == mid, this means that we checked low and mid and since both are not target, we send index of low where we would place target (shifting everything else to right)
                    return low
            else:                               # if the target is more than the value at mid, make low = mid + 1
                low = mid + 1
                if high == mid:                 # if we get at the case where high == mid, thi smeans that we checked high and mid and since both are not target, we return the index where target would go, which is high + 1
                    return high + 1
        