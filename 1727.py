class Solution:
    def largestSubmatrix(self, matrix) -> int:
        n = len(matrix)
        m = len(matrix[0])
        answer = 0

        for i in range(n):
            for j in range(m):
                if i>0 and matrix[i][j] == 1:
                    matrix[i][j]+=matrix[i-1][j]
            tmp_row = sorted(matrix[i],reverse = True)
            for k,value in enumerate(tmp_row):
                answer = max(answer,(k+1)*value)

        return answer 
    
    
l=[[0,0,1],[1,1,1],[1,0,1]] 




a = Solution()
a.largestSubmatrix(l) 