<<<<<<< HEAD
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        last = mid = head

        while last and last.next :
            last = last.next.next
            mid = mid.next 

        prev = None 

        while mid :
            tmp = mid.next 
            mid.next = prev 
            prev = mid 
            mid = tmp
        

        lft , rght = head , prev 
        while rght :
            if rght.val != lft.val :
                return False 

            lft = lft.next 
            rght = rght.next
        return True 
        
     



=======
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        last = mid = head

        while last and last.next :
            last = last.next.next
            mid = mid.next 

        prev = None 

        while mid :
            tmp = mid.next 
            mid.next = prev 
            prev = mid 
            mid = tmp
        

        lft , rght = head , prev 
        while rght :
            if rght.val != lft.val :
                return False 

            lft = lft.next 
            rght = rght.next
        return True 
        
     



>>>>>>> 86d1479054b46193473a840b95d6acc626908e7b
        