class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                val = nums[left] + nums[right]
                if val == target:
                    return [left, right]