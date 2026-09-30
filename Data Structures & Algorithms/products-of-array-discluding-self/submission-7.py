class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        # L
        L = []
        R = []
        for i  in range(len(nums)):
            if not L:
                L = [1]
            else:
                L.append(L[-1]*nums[i-1])
            if not R:
                R = [1]
            else:
                R.append(R[-1]*nums[len(nums)-i])

            
        return [L[i]* R[len(nums)-1-i] for i in range(len(nums))]