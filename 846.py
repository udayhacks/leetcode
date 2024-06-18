class Solution:
    def isNStraightHand(self, hand, groupSize) -> bool:
        import collections
        hand.sort()
        
        if len(hand) //groupSize <  groupSize :return False
            
        c = {}
        for i in hand :
            if i in c :
                c[i] +=1
            else:
                c[i] = 1
                
                
        #[2,3,3,3,4,5,5,6,7]     = 3
        
        #[2,3,4] [5,6,7] [2 =1,3 =3 ,4=1,5 = 3,6 = 1 ,7 = 1]    
        
        
        
        
        
        
        
        
        
        
        
        
        
a = Solution()
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
a.isNStraightHand(hand,groupSize)