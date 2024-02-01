def permuations(string,i= 0,ans=[]):
    if i ==len(string):
        aa="".join(string)
        ans.append(aa)       
    else:
         for j in range(i,len(string)):
            word = list(string)

            word[i],word[j] = word[j],word[i]
            permuations(word,i+1,ans)
         
    return ans       
       
 
        



print(permuations("yup"))


def permuations(string,i= 0,ans=[]):
    if i ==len(string):
        ans.append(string)       
    else:
         for j in range(i,len(string)):
            string[i],string[j] = string[j],string[i]
            permuations(string,i+1,ans)
         
    return ans       
       
 
        
def p(nums,i ,res=[]):
            if i == len(nums):
                res.append(nums)
            else:
                for j in range(i,len(nums)) :
                    nums[i],nums[j] = nums[j],nums[i] 
                    p(nums,i+1,res)

            return res
        
        
print(p([1,2,3],0))
        
print(permuations([1,2,3]))