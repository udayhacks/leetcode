


class ListNode():
    def __init__(self,val = 0 )-> None:
        self.val = val
        self.next = None





class Solution:
    def mergeTwoLists(self, list1, list2):

        uday = ListNode()
        curr = uday

        while list1 and list2 :
            if list1.val <= list2.val :
                curr.next = ListNode(list1.val)
                curr.next.next = ListNode(list2.val)
                list1 = list1.next
                list2 = list2.next
            else :
                
                curr.next.next = ListNode(list1.val)
                curr.next = ListNode(list2.val)
                list1 = list1.next
                list2 = list2.next
        
        curr.next = list1 if list1 else list2




        return uday.next 
        
        


[1,2,4]

[1,3,4]





l = ll=ListNode(1)

l.next = ListNode(2)
l.next.next = ListNode(4)



k =kk= ListNode(1)
k.next = ListNode(3)
k.next.next = ListNode(4)




a = Solution() 
p = a.mergeTwoLists(ll,kk)

while l :
    print(p.val)
    p= p.next
    

