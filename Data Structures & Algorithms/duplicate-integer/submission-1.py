class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            dic[num] = True
        if len(dic.keys()) < len(nums): return True
        else : return False

