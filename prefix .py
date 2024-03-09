

arr = [1,-1,2,3,5,-9,10]

k = 5 
s = 0 
c= 0
hp = {0:1}
for i in range(len(arr)): 
    s+=arr[i]
    
    if s==k :
        c+=1
        
    rem = s-k
    if rem in hp :
        hp[rem] +=1
        c+=hp[rem]
        
    else:
        hp[rem] =1 
        
        
print(c)









from collections import defaultdict






def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr) # size of the given array.
    mpp = defaultdict(int)
    preSum = 0
    cnt = 0

    mpp[0] = 1 # Setting 0 in the map.
    for i in range(n):
        # add current element to prefix Sum:
        preSum += arr[i]

        # Calculate x-k:
        remove = preSum - k

        # Add the number of subarrays to be removed:
        cnt += mpp[remove]

        # Update the count of prefix sum
        # in the map.
        mpp[preSum] += 1

    return cnt


if __name__ == '__main__':
    arr = [1,-1,2,3,5,-9,10]
    k = 5
    cnt = findAllSubarraysWithGivenSum(arr, k)
    print("The number of subarrays is:", cnt)    
                    

        
    
    
    
    
    
    
    


