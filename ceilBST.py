def ceiling(root , k ) :
    curr = root 
    res = None 
    aa = curr.val 
    while curr :
        if root.val ==k:
            return root
        elif root.val < k :
            curr = root.right 
        else :
            res = curr.val 
            curr = curr.left 
            
    return res