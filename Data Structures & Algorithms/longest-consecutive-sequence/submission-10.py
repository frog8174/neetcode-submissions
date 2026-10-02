
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        S = set(nums)
        max_length = 0
        for num in S:
            if num - 1 not in S:
                head = num 
                length = 1
                while (head+1) in S:
                    head += 1
                    length += 1
                if length > max_length: max_length = length
        return max_length
            
            