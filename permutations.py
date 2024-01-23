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