class Solution:
    def isValid(self, s: str) -> bool:
        
        left = ["(", "[", "{"]
        table = {")":"(", "]":"[", "}":"{"}
        brackets = []
        for b in s:
            # left bracket
            if b in table.values():
                brackets.append(b)
            # right bracket
            else:
                if not brackets or brackets[-1] != table[b]:
                    return False
                brackets.pop()

        return not brackets
