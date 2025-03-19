class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        odblak = ["a","c","e","g"]              
        k = list(coordinate1)
        k1 = list(coordinate2)
                  
                  
        if( (k[0] in odblak and k[1] %2!= 0 ) and (k1[0] in odblak and k1[1] %2 != 0 ) ) or (   (k[0] in odblak and k[1] %2== 0 ) and (k1[0] in odblak and k1[1] %2 == 0 ) )  :
                  return True
        return False
        
    
                  
a = Solution()
a.checkTwoChessboards("a1","b3")