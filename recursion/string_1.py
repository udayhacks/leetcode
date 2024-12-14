class Solution:
        def countOfSubstrings(self, word: str, k: int) -> int:
            def valid(s,k):
                cv = []
                cs = [] 
                if len(s) >= k+5:
                
                    v = ["a","e","i","o","u"]
                    
                    
                    for i in s :
                        if i  in v :
                            cv.append(i)
                        else:
                            cs.append(i)

                return len(set(cv)) ==5 and len(cs)== k 
            
            
                
            words = list(word)
            c= i=0 
            ans = []
            
            
            for j in range(len(words)) :
            
        
                if valid(word[:j+1],k):ans.append(words[i:j+1])
                while j-i  > k+4  :
                    i+=1
                    if valid(word[i:j+1],k):ans.append(word[i:j+1])
                    
                    
            return len(ans)
                    
                            
                
            
            
             
            
      
        

        







a =Solution()
j = a.countOfSubstrings("uiuuoae", k = 0)
print(j)

        