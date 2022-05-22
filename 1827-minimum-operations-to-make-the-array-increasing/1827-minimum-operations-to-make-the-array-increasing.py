class Solution:
    def minOperations(self, nums: List[int]) -> int:
            if len(nums) < 2:
                return 0

            result = 0
            for i in range(1, len(nums)):
                if nums[i-1] >= nums[i]:
                    result += nums[i - 1] - nums[i] + 1
                    nums[i] += nums[i - 1] - nums[i] + 1

            return result