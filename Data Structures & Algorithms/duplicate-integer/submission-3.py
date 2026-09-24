class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = True
            else:
                return True
        return False
        
