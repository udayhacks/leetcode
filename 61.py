











































class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

"""

class Solution:
    def rotateRight(self, head, k: int) :
        if not head or not head.next or k==0:
            return head 
        cur,size=head,1
        while cur.next:
            size+=1
            cur=cur.next    
        k=k%size
        k=size-k
        cur.next=head
        while k:
            cur=cur.next
            k-=1    
        head=cur.next
        cur.next=None
        return head


"""







class Solution :
    def rotateRight(self, head, k: int) :
        if not head or not head.next or k == 0 :
            return head 
        
        cur , size = head , 1
        
        while cur.next :
            size +=1
            cur = cur.next
            
            
        k = k % size
        k = size - k 
        
        cur.next =  head 
        
        while k :
            cur = cur.next 
            k-=1
            
        head = cur.next 
        cur.next = None
        return head
    






















head = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)


head.next  = b
b.next = c
c.next = d
d.next = e



a = Solution()
l = a.rotateRight(head,2)


curr = l 


while curr :
    print(curr.val)
    curr = curr.next 
    
    
    

    







        