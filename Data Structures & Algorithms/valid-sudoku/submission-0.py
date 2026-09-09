class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for i in range(9):
            seen=set()
            for j in range(9):
                item = board[i][j]
                if item == ".":
                    continue
                if item in seen:
                    return False
                
                seen.add(item) 
        #columns 
        for i in range(9):
            seen=set()
            for j in range(9):
                item = board[j][i]
                if item == ".":
                    continue
                if item in seen:
                    return False
                
                seen.add(item)
    
        #boxes 
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen=set()
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        item = board[row][col]
                        if item == ".":
                            continue
                        if item in seen:
                            return False
                        seen.add(item)
        return True