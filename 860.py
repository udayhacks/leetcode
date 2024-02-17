


class Solution:
    def lemonadeChange(self, bills) -> bool:
        amount=bills[0]
        if bills[0]  > 5 :
            return False
        for i in range(len(bills)):
            if bills[i] > 5 :
                amount-= bills[i]-5
                
                if amount< 0 :
                    return False

            amount+= bills[i]-5    

        return True



a= Solution()
a.lemonadeChange([5,5,10,10,5])