class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:

        r = len(matrix)
        c = len(matrix[0])

        i = 0 
        j = c-1


        while  i < r and j >= 0 :

            if matrix[i][j] == target :
                return True 
            elif  matrix[i][j] < target :
                i+=1
            else :
                j-=1

        return False




a = Solution()
print(a.searchMatrix([[-1,3]],-1))