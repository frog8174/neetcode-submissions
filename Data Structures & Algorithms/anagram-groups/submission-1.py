import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        d = collections.defaultdict(list)
        for s in strs:
            key = 1
            for char in s:
                key *= primes[ord(char) - ord('a')]

            d[key].append(s)           
        
        return list(d.values())