class Solution:
    def luckyNumbers (self, matrix):

        l = []
        h = []

        c = len(matrix[0])
        r = len(matrix)


        for i in range(r):
            res = 10**5
            for j in range(c):
                res = min(res,matrix[i][j])
            l.append(res)


        for j in range(c):
            res = 0 
            for i in range(r):           
                res = max(res,matrix[i][j])
            h.append(res) 

        res = []
        
        
        for i in range(len(h)):
            if h[i] in l : res.append(h[i])
        
        return res



a = Solution()
k = a.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]])
l = a.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]])
h = a.luckyNumbers([[7,8],[1,2]])
ans = [k,l,h]
for i in ans :
    print(i)


            

        