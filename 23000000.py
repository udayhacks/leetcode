class Solution:
    def successfulPairs(self, spells, potions, success: int) :
        ans = []
        for s in  spells : 
            c = 0 
            i =0 
            j = len(potions) -1
          
            while i <= j :
                if s*j >= success :
                    c+=1
                if s*i >= success:
                    c+=1
            ans.append(c)


        return ans
