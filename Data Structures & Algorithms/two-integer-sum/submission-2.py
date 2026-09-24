class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set(nums)
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in s:
                for j, num in enumerate(nums[i+1:]):
                    if num == remaining:
                        return [i, i+j+1]
            