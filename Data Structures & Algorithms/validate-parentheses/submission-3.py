class Solution:
    def isValid(self, s: str) -> bool:
        
        left = ["(", "[", "{"]
        table = {")":"(", "]":"[", "}":"{"}
        brackets = []
        for b in s:
            if not brackets:
                brackets.append(b)
                continue
            
            if b in left:
                brackets.append(b)
            else:
                if brackets[-1] == table[b]:
                    brackets.pop()
                else:
                    return False

        return len(brackets) == 0
