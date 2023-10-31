def Guest(arr,lev):
    
    arr.sort()
    lev.sort()
    
    i = res = c= 1
    j = 0 
    n = len(arr)
    time = arr[0]
    
    while i < n and j < n :
        if arr[i] <= lev[j] :
            c+=1
            i +=1
        else :
            c-=1
            j+=1
        if res < c :
            res = c 
            time = arr[i-1]
    return time , res 



arr = [900,600,700]
lev =[1000,800,730]

Guest(arr, lev)
