class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    

        d = {}
        left = 0
        res = 0
        max_freq = 0
        max_freq_ch = ""
        for right in range(len(s)):

            ch = s[right]
            if ch in d: 
                d[ch] += 1
            else:
                d[ch] = 1

            if d[ch] > max_freq: 
                max_freq = d[ch]
                max_freq_ch  = ch

            # 除了最頻繁字母之外的出現次數 > 可替換次數
            while (right - left + 1) - max_freq > k:
                ch_left = s[left]
                d[ch_left] -= 1
                left += 1



            
            res = max(right - left + 1, res)
        
        return res