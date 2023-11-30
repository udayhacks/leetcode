def subarr(arr , sum ):
    n = len(arr)
    curr  = 0 
    count = 0 
    hashmap = {}
    
    for i in range(n):
        curr += arr[i]
        if curr == sum :
            count +=1 
        if curr -sum in hashmap :
            count +=hashmap[curr-sum]
            
        if curr in hashmap :
            hashmap[curr] +=1
        else :
            hashmap[curr] =1
    return count 



subarr([10,-2,2,-20,10],-10)