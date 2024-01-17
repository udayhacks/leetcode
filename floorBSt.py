def floorBst(root, k):
    curr = root
    res = None 
    while curr:
        ll = curr.val
        
        if curr.val == k :
            return root
        elif curr.val > k :
            curr = curr.left 
        else :
            res = curr.val 
            curr = curr.right 
            
    return res 




            
    