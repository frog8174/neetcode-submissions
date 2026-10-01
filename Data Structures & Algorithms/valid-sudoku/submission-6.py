class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                value = int(board[i][j]) - 1
                mask = 1 << value

                box_index = (i // 3) * 3 + (j // 3)

                if (rows[i] & mask) or (cols[j] & mask) or (boxes[box_index] & mask):
                    return False
                rows[i] |= mask
                cols[j] |= mask
                boxes[box_index] |= mask
        return True