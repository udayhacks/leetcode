def selectionSort(arr):
    
    n = len(arr) 
    for i in range(n) :
        j = arr.index(min(arr[i:]))
        arr[j] ,arr[i] = arr[i],arr[j]
        
        
    print(arr)


selectionSort([2 ,13 ,4 ,1 ,3 ,6 ])