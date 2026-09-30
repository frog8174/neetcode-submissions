class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        

    def decode(self, s: str) -> List[str]:
        
        ans=[]
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            word_length = int(s[i:j])
            i = j+1+word_length
            ans.append(s[j+1:i])
        return ans

            
