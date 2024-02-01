#subset sum 

def subset_sum(arr,i,s,ans):
    if i ==len(arr):
        ans.append(s)
        
    else:
        subset_sum(arr,i+1,s+arr[i],ans)
        subset_sum(arr,i+1,s,ans)
        
        
    return ans



arr  = [3,1,2]

print(subset_sum(arr,0,0,[]))