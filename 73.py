class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        

        row = len(matrix)
        colm = len(matrix[0])
        col = False


        for r in range(row):
            for c in range(colm):
                if matrix[r][c] == 0 :
                    matrix[r][0] = 0 
                    if c!= 0 :
                        matrix[0][c] = 0 
                    else:
                        col= True 


        for r in range(1,row) :
            for c in range(1, colm) :
                if matrix[r][c] != 0:
                    if matrix[r][0] == 0 or matrix[0][c] == 0 :
                        matrix[r][c]  = 0 


        if matrix[0][0]  == 0 :
            for r in range(colm):
                matrix[0][r] =0 
        if col : 
            for c in range(row):
                matrix[c][0] =0 
                
                
                
a   = Solution()
a.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]
)