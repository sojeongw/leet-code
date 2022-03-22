class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        sum = 0
        
        for i in nums:
            sum += i
            
        diff = abs(goal - sum)
        
        if diff == 0:
            return 0
        
        if diff % limit == 0:
            return diff // limit
        
        return (diff // limit) + 1