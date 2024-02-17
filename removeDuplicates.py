def removeDuplicates(arr,n):
    
    
    i = 1
    j = 0 
    while i <= n-1 :
        
        if arr[j]== arr[i]:
            
            while i < -1 and j < n-1 and arr[j] == arr[i] :
                i+=1
            j+=1
            arr[j] = arr[i]
            continue
        i+=1
        j+=1
            
        
    return arr[:j]
           
    
    
    
    
n = 5
arr = [1, 2 ,2 ,2 ,3]



a=removeDuplicates(arr,n)
print(a)
