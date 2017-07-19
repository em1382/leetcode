class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(x) for x in str(int(''.join(str(d) for d in digits)) + 1)]
