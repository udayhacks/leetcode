

        
class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr,n):
        return self.mergeSort(arr,n)
    def mergeSort(self, arr, n):
        if n < 2:
            return 0
        mid = n //2
        left = arr[:mid]
        right = arr[mid:]
        c = 0
        
        c += self.mergeSort(left, mid)
        c += self.mergeSort(right, n - mid)
        c += self.merge(arr, left, right, mid, n-mid)
        return c
        
    def merge(self, arr, left, right, mid, n):
        i = 0
        j = 0
        k = 0
        c = 0
        
        while i < mid and j < n:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                c += mid - i
                j += 1
            k += 1
        while i < mid:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < n:
            arr[k] = right[j]
            j += 1
            k += 1
        
        return c
