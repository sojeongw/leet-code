class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        array = s.split(" ")
        result = array[0]

        for i in range(1, k):
            result += " " + array[i]
            
        return result