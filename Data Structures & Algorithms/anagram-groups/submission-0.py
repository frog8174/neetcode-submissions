class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            counts = [0]*26
            for char in s:
                counts[ord(char) - ord('a')] += 1

            key = tuple(counts)
            
            if key not in d:
                d[key] = [s]
            else:
                d[key].append(s)            
        
        return list(d.values())