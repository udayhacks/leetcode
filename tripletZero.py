



class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        
        
        
        
        for i in range(n-1) :
            for j in range(i+1,n-1) :
                x = arr[i]+arr[j]
                
                if -x in arr and arr.index(-x) != i and arr.index(-x) != j:
                    return 1 
        return 0
        
        #code here
        
        
        
        
import sys 
sys.stdin = open("inp.txt","r")
sys.stdout = open("out.txt","a")

n = int(input())
k = list(map(int, input().split()))




a = Solution()
print(a.findTriplets(k,n))


