class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        flag = 0
        for num in nums:
            if num == 0:
                flag = 0
            else:
                flag += 1
            
            if flag > ans:
                ans = flag

        return ans
