class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        columns = len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = columns - 1
        row = -1

        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                row = mid
                break
        
        if row == -1:
            return False
        
        while left <= right:
            mid_l = (left+ right) // 2
            if target > matrix[row][mid_l]:
                left = mid_l + 1
            elif target < matrix[row][mid_l]:
                right = mid_l - 1
            else:
                return True
        return False
        