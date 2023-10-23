def demo (arr):
    n= len(arr)
    l = 0 
    h = n-1 
    k = 0
     
    while l<=h :
        m = (l+h)//2
        if (arr[h] -arr[m] == 0 and h!=m)  or ( arr[m]-arr[l] == 0 and m!=l):
            k = arr[m]
            break 
        if arr[h]-arr[m]  == h-m:
            h = m-1
        else :
            l = m+1
        
    j = n-(arr[n-1]-arr[0])
    return [k,j]
            
demo([5,6,7,8,9,9,9,10])            