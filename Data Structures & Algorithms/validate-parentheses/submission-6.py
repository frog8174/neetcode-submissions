class Solution:
    def isValid(self, s: str) -> bool:
        
        left = ["(", "[", "{"]
        table = {")":"(", "]":"[", "}":"{"}
        brackets = []
        for b in s:

            if brackets:
                if b in table.values():
                    brackets.append(b)
                else:
                    if brackets[-1] == table[b]:
                        brackets.pop()
                    else:
                        return False
            else: brackets.append(b)

        return len(brackets) == 0
