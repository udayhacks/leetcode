def subarray(arr):
    l = []
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            l.append(arr[i:j+1])
    return l

a = [1,2,3,4]
print(len(subarray(a)))



""" total subarrays of an array = n*(n+1)/2 """
