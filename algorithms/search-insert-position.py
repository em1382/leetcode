class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except:
            if target < nums[0]:
                return 0
            elif target > nums[-1]:
                return len(nums)
            for i in range(len(nums) - 1):
                if nums[i] < target and nums[i + 1] > target:
                    return i + 1
