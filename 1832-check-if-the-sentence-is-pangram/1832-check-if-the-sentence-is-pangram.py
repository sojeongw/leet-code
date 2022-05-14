class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        removed_duplicates = set(sentence)

        if len(removed_duplicates) == 26:
            return True
        else:
            return False