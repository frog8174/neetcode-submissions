import operator
class Solution:
    def is_vaild_number(self, s: str) -> bool:
        try:
            float(s)  
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        nums = []
        for s in tokens:
            if self.is_vaild_number(s):
                nums.append(s)
                continue
            sec_num = int(nums.pop())
            fir_num = int(nums.pop())
            
            nums.append(operations[s](fir_num,sec_num))
        
        return int(nums[-1])

