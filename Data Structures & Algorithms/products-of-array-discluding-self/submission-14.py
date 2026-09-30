class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        postfix = 1
        # need a reverse index of i
        for i in list(range(len(nums)))[::-1]:
            ans[i] *= postfix
            postfix *= nums[i] 

        return ans