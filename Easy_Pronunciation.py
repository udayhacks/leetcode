#class Solution:
def fun(s):
  d = {'a':1,
        'e':1,
        'i':1,
        'o':1,
        'u':1
        }
  count = 0 
  ans =0 
  for i in s :
    if d.get(i,0) == 0:
      count+=1
      ans = max(ans,count)
      if ans >= 4 :
        break
    else:
    count = 0 
      
  if ans >= 4 :
    print("NO")
  else:
    print("YES")
    
fun("tryst") #YES
      
  
      