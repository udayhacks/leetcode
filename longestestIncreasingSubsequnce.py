a = [3,4,2,8,10]  


# longest increasing subsquences 
# 

# def func(arr) :
    
#     n = len(arr)
#     temp = [1]*n
#     res = temp[0]
    
#     for i in range(1,n) :
#         for j in range(0,i):
#             if  arr[i] > arr[j] :
#                 temp[i] = max(temp[i],temp[j]+1)
                 
#         res = max(res,temp[i])
        
#     return res 





def ceiling(arr,x ):
    
    l = 0 
    r = len(arr) -1
    
    while l < r :
        m= (l+r)//2
        if arr[m] >= x:
            r = m
        else:
            l = m+1
            
    return r



def func2(a):
    
    tail = [a[0]]
    
    for i in range(1,len(a)):
        if a[i] > tail[-1]:
            tail.append(a[i])    
        else:
            c = ceiling(tail,a[i])
            tail[c] = a[i]
            
    return len(tail)


a = [3,4,2,8,10]  
print(func2(a)) 
  

    
       
        

    
    