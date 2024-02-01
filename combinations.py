def combination(arr,i,target ,ds,ans) :
    if i == len(arr) :
        if target ==0 :
            ans.append(ds[:])
        
        
    else:
                
        if arr[i] <= target :
            ds.append(arr[i])
            combination(arr,i,target-arr[i],ds,ans)
            ds.pop()
        combination(arr,i+1,target,ds,ans)
        
        
    return ans
        
        
        
        su
arr = [2,3,6,7]
k = 7
da = []
ans = []

j = combination(arr,0,k,da,ans)
print(j)  

   
            
    