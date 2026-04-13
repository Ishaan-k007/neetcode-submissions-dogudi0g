class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # plan:
        # preform a binary search to determine which row it is in
            # or an approach could do check last digit of row and do most recent >=
            # then im going to do an exact condition binary search 

        L = 0
        R = len(matrix) 
        while L < R:
            print(L,R)
            mid = (L + R) // 2

            if matrix[mid][-1] == target:
                return True

            if matrix[mid][-1] <target:
                L = mid + 1

            else:
                R = mid

            

        row_index = L
        if row_index > len(matrix) - 1:
            return False
        print(row_index)
        L = 0
        R = len(matrix[row_index]) - 1 

        while L <= R:
            mid = (L + R) // 2

            if matrix[row_index][mid] == target:
                return True

            elif matrix[row_index][mid] < target:
                L = mid + 1

            else:
                R = mid - 1



        return False



        