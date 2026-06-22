class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 90 clockwise
        # transpose matrix 
        # reverse each row

        # 90 anti clockwise
        # transpose matrix 
        # reverse each column

        # 180
        # reverse each row 
        # reverse each column

        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
        for i in range(len(matrix)):
            matrix[i].reverse()
     
        
        


        