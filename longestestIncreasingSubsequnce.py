a = [3,4,2,8,10]  


# longest increasing subsquences 
# 

def func(arr) :
    
    n = len(arr)
    temp = [1]*n
    res = temp[0]
    
    for i in range(1,n) :
        for j in range(0,i):
            if  arr[i] > arr[j] :
                temp[i] = max(temp[i],temp[j]+1)
                
        res = max(res,temp[i])
        
    return res 



print(func(a))
        
        
        

    
    