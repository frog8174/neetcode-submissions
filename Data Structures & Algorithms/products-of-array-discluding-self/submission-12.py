class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        L = [1]
        R = [1]
        for i  in range(1,n):
            L.append(L[-1]*nums[i-1])
            R.append(R[-1]*nums[n-i])

            
        return [L[i]* R[n-1-i] for i in range(n)]