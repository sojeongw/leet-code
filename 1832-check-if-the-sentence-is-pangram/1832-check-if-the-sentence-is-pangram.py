class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        dic = {}

        for s in sentence:
            dic[s] = 1

        return len(dic) == 26