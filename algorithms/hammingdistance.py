class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        diff = 0
        for ix, iy in zip(format(x, '08b'), format(y, '08b')):
            if ix != iy: diff += 1
        return diff
