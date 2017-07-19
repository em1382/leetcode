class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for letter in magazine:
            if letter in ransomNote:
                ransomNote.replace(letter, '')
        if ransomNote == '':
            return True
        return False
