class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1 = "".join(sorted(s1))
        windowSize = len(s1)
        right = 0
        left = 0
        
        for right in range(len(s2)):
            
            # 只要遇到例外，左邊界壓縮
            if s2[right] not in s1:
                left = right+1
                continue

            # char 在 s1 裡面，目前到windowSize
            if (right-left+1) == windowSize:
                sw = "".join(sorted(s2[left:right+1]))
                if s1 == sw:
                    return True
                else: left += 1

        return False