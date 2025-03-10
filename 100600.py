class Solution:
    def numOfUnplacedFruits(self, fruits, baskets) -> int:
        n = len(fruits)
        flag = True
        count =0 
        for i in fruits:
            for j in range(n):
                if i <= baskets[j] :
                    baskets[j] = 0
                    flag = False
                    break
            if flag :
                count+=1
                flag = True
      
            
        return count
    
a = Solution()
fruits = [4,2,5]
baskets = [3,5,4]

a.numOfUnplacedFruits(fruits,baskets)