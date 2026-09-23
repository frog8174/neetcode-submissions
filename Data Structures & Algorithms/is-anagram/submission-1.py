class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        
        for i , j in zip(s,t):
            if i not in d:
                d[i] = 1;
            else: 
                d[i] += 1
                if d[i] == 0: del d[i];
            
            if j not in d:
                d[j] = -1;
            else: 
                d[j] -= 1
                if d[j] == 0: del d[j];


        if len(d.keys()) == 0: return True
        else: return False