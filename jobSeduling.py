def job (arr,t):
    n = len(arr)
    arr.sort(key= lambda x :x[1],reverse= True)
    result =[False]*t
    res = 0
    for i in range(n) :
        k = min(t-1,arr[i][0]-1)
        for j in range(k,-1,-1) :
            if result[j] == False:
                result[j] = True
                res+=arr[i][1]
                break
    return res


arr= [(4,50),(1,5),(1,20),(5,10),(5,80)]
t = 5 
print(job(arr,t))
    