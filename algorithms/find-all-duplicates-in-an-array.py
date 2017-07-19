class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        seen = set()
        for num in nums:
            if num in seen:
                res.append(num)
            else:
                seen.add(num)
        return res
