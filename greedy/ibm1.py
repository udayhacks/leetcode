def boxnumber(i):
  sum = 0 
  while i >0 :
    sum+=(i%10)
    i= i//10

  return sum

df = {}
ans = 0 


mn = min(nums)
mx = max(nums)
for i in range(mn,mx+1):
  k = boxnumber(i)
  if k in df :
    df[k] +=1
    

  else:
    df[k] =1
  if df[k] > ans :
      ans = df[k]

print(ans)