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
            '/': lambda a, b: int(a / b)
        }
        nums = []
        for token in tokens:
            if token not in operations:
                nums.append(int(token))  
            else: 
                sec_num = int(nums.pop())
                fir_num = int(nums.pop())
                
                nums.append(operations[token](fir_num,sec_num))
        
        return nums[0]

