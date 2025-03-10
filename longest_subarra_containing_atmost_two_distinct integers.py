
import array


class Solution:
    def totalElements(self,arr):
        a  = -1
        ai = 0
        b =   arr[0]
        bi = 0
        ans = 1 
        pos = 0
        
        
        n = len(arr)
        for j in range(1,n):
            if arr[j] != b and a== -1:
                a = b
                ai = bi 
                b = arr[j]
                bi = j
            elif arr[j] != b and arr[j] != a:
                pos = bi
                a = b
                b = arr[j]
                ai = bi
                bi = j
                
                
            ans = max(ans,j - pos )
            
        return ans 
            
                
            
a = Solution()

arr = [3,3,3,1,2,1,1,2,3,3,4]
arr = [85, 12, 69, 8, 34, 53, 72, 60, 29, 48, 32, 66, 19, 27, 6, 27, 44, 44, 60, 80 ,22, 73, 65, 8, 62, 81, 41, 20, 76, 12, 6, 65, 45, 1 ,90 ,84 ,74 ,32 ,90 ,44 ,27 ,79 ,91, 21 ,36 ,82 ,70, 8, 83, 59, 39, 20, 70, 15 ,5 ,28 ,29, 54, 51 ,34 ,51 ,1 ,71 ,56 ,15 ,29 ,68, 8 ,68 ,51, 7 ,72 ,70 ,6, 9, 39 ,21, 2 ,22 ,18 ,36 ,79 ,10 ,84 ,29 ,8 ,42 ,22 ,1 ,42 ,62]
print(a.totalElements(arr))