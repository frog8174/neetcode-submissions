class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #dvdf
        d = {}
        left = 0
        res = 0
        for right in range(len(s)):
            ch = s[right]
        
            if ch in d and d[ch] >= left:
                left = d[ch] + 1
            d[ch] = right
            res = max(right-left+1, res)
 

        return res
