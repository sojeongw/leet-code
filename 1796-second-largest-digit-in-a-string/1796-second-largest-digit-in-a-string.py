class Solution:
    def secondHighest(self, s: str) -> int:
        result = []

        for value in s:
            if value.isdecimal() and value not in result:
                result.append(value)

        if len(result) < 2:
            return -1
        
        result.sort()

        return int(result[-2])
