class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        L = 0
        R = len(matrix)

        while L < R:
            mid = (L + R) // 2

            if matrix[mid][-1] < target:
                L = mid + 1
            else:
                R = mid
        
        # L contains the row with target
        if L == len(matrix):
            return False
        
        row = L
        
        L = 0
        R = len(matrix[row])
 
        while L <= R:
            mid = (L + R) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                L = mid + 1
            else:
                R = mid - 1
        return False 


        
          
