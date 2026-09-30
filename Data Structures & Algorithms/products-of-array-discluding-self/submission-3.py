class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        # L
        L = []
        
        for i  in range(len(nums)):
            if not L:
                L = [1]
            else:
                L.append(L[-1]*nums[i-1])
        
        # print("L: ", L)

        R = []
        for i  in range(len(nums)):
            if not R:
                R = [1]
            else:
                R.append(R[-1]*nums[len(nums)-i])
        # print("R: ", R)

            
        R = R[::-1]
    
        return [L[i]* R[i] for i in range(len(nums))]