




def countSubarraysDivByK(arr, k):
    count = {0: 1}  
    prefix_sum = 0
    result = 0
    
    for num in arr:
        prefix_sum += num
        remainder = prefix_sum % k
        # Adjust for negative remainders
        remainder = (remainder + k) % k
        
        # Add the count of this remainder to the result
        result += count.get(remainder, 0)
        
        # Update the count of this remainder in the hash map
        count[remainder] = count.get(remainder, 0) + 1
    
    return result




print(countSubarraysDivByK([4,5,0,-2,-3,1],5)) # 7