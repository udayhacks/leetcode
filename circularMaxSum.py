from maxSumSubarry import maxSubarr

l = [5,-2,3,4]

l =[2,3,-4]

# circular sum = max(minsum,maxsum)


def cirSumArr(l):
    k = maxSubarr(l)
    e = l[0] 
    n = len(l)
    u = l[0]
    res = l[0] 
    
    for i in range(1, n):
        u+=l[i]
        e = min (l[i]+e,l[i])
        res = min(res,e) 
    return max(k,u-res)



cirSumArr(l)
    
    
    
    
    