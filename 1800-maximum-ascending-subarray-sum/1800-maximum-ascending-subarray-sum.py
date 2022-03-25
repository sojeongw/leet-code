class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_value = nums[0]
        sum_value = nums[0]

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                sum_value += nums[i]
                if max_value < sum_value:
                    max_value = sum_value
            else:
                sum_value = nums[i]

        return max_value