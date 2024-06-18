
import sys

def maxSubarraySum(arr, n):
    maxi = -sys.maxsize-1 # maximum sum
    sum = 0
    e = s = 0
    ee =ss = 0
    for i in range(n):
        sum += arr[i]

        if sum > maxi:
            maxi = sum
            ss= s
            ee = i+1
            
             
            

        # If sum < 0: discard the sum calculated
        if sum < 0:
            sum = 0
            s = i+1

    # To consider the sum of the empty subarray
    # uncomment the following check:

    #if maxi < 0: maxi = 0

    return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maxSubarraySum(arr,len(arr))
k = sum(arr[3:7])