class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        d = {}
        res = 0
        flag = 0
        for i in range(len(s)):
            ch = s[i]
            # d[ch] >= left
            if ch in d:
                if d[ch] >= flag:
                    flag = d[ch] + 1

            d[ch] = i 


            res = max(i-flag+1, res)
            
                
        return res
