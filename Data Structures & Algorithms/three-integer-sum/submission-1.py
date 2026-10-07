class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        res = []
        for i in range(length):
            
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            numL = nums[i]
            target =  -numL
            j = i + 1
            k = length - 1
            
            while j < k:    
                numM = nums[j]
                numR = nums[k]
                total = numM + numR
                if total > target:
                    k -= 1
                elif total < target:
                    j += 1
                else:
                    res.append([numL,numM,numR])
                    k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                    
        return res

            