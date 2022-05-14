class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        dic = {}
        for s in sentence:
            dic[s] = 1
        if len(dic) == 26:
            return True
        return False