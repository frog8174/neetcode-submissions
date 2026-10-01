class Solution:
    
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                
                if element == ".": continue
                box_index = (i // 3) * 3 + (j // 3)

                if element in row_sets[i]: return False
                row_sets[i].add(element)

                if element in col_sets[j]: return False
                col_sets[j].add(element)
               
                    

                if element in box_sets[box_index]: return False
                box_sets[box_index].add(element)

             
        return True
