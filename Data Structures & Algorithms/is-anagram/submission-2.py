class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        d = {}
        for i, j in zip(s, t):
            d[i] = d.get(i, 0) + 1
            if d[i] == 0: del d[i]

            d[j] = d.get(j, 0) - 1
            if d[j] == 0: del d[j]


        if len(d.keys()) == 0: return True
        else: return False