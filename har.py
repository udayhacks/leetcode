def count_all_subarrys(arr,  n,k):
    # count all subarrays
    res = 0
    for i in range(n):
        summ = 0
        for j in range(i, n):
 
            # Calculate required sum
            summ += arr[j]
 
            # Check if sum is equal to
            # required sum
            if summ == k:
                res += 1
    return res
 
print(count_all_subarrys([0,1,0],3,1))