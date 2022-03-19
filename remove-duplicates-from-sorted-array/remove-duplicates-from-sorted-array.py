class Solution(object):
    def removeDuplicates(self, nums):
        count = 1
        if(len(nums)==1):
            return count
        while count!=len(nums):
            if nums[count] == nums[count-1]:
                nums.pop(count)
            else:
                count += 1