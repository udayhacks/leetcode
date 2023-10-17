class node :
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    

a = node(1)
b = node(2)
a.next = b 
c = node(3)
b.next = c 

print(a)
print(a.next)


head = b
print(head.data)
d = {} 

while head :
    d[head]  = head.data
    head = head.next
print(d)
    
