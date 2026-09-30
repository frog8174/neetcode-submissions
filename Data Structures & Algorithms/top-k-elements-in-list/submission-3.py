class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        D = {}
        for num in nums:
            if num not in D:
                D[num] = 1
            else: D[num] += 1
       
        return sorted(D, key = D.get, reverse=True)[:k]

        