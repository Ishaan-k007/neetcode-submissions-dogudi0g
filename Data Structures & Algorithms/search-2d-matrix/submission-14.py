class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        
        UP = 0
        DOWN = len(matrix) - 1


        while UP < DOWN:
            mid = (UP + DOWN) // 2

            if matrix[mid][-1] < target:
                UP = mid + 1
            else:
                DOWN = mid
        
        cor_row = UP
        L = 0 
        R = len(matrix[0]) -1 


        while L <= R:
            mid = (L + R) // 2

            if matrix[cor_row][mid] == target:
                return True
            elif matrix[cor_row][mid] < target:
                L = mid + 1
            else:
                R = mid - 1
        return False   
