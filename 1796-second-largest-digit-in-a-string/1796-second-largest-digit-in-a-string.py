class Solution:
    def secondHighest(self, s: str) -> int:
        result = []

        for value in s:
            if value.isdecimal() and value not in result:
                result.append(value)

        if len(result) == 0 or len(result) == 1:
            return -1
        
        result.sort()

        return int(result[-2])
