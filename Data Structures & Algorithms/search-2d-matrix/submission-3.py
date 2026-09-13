class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        low=0
        high=(ROWS*COLS)
        while low<high:
            mid=(low+high)//2
            row = mid // COLS
            col = mid % COLS
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                low+=1
            else:
                high-=1
        return False
