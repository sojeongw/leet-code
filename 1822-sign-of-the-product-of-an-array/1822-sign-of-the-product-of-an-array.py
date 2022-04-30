class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
    
        count = 0
        for n in nums:
            if n < 0:
                count += 1

        if count % 2 == 1:
            return -1
        else:
            return 1