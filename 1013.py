class Solution:
    def canThreePartsEqualSum(self, arr):
        kk = sum(arr)
        k = kk//3
        c= 0
        s = 0
        for i in range(len(arr)):
            s+=arr[i]
            if s == k :
                c+=1
                s = 0 
                
        if c >= 3 and kk%3 == 0  :
            return True
        return False
            
            
        
    
    
    
a= [0,2,1,-6,6,-7,9,1,2,0,1]
b = [0,2,1,-6,6,7,9,-1,2,0,1]
c = [3,3,6,5,-2,2,5,1,-9,4]
d = [3,3,6,5,-2,2,5,1,-8,4]
e = [1,1,1,1]








ans = Solution()

for i in [a,b,c,d,e]:
    print(sum(i))
    print(ans.canThreePartsEqualSum(i))

print(ans.canThreePartsEqualSum(e))