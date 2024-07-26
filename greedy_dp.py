


from collections import defaultdict 

def func(arr):
    
    mx = 0 
    n = len(arr)
    
    for i in range(len(arr)) :
        mx = max(arr[i:i+arr[i]])
        if mx > n-1:
            return False
        
    return True 

a = [3,2,1,0,4]

func(a)

            