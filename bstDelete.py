def getSucc(root):
    curr = root
    while curr.left :
        curr = curr.left
    return curr.val
        

def delete(root, k ):
    
    def getSucc(root):
        curr = root
        kk = curr.val
        while curr.left :
            curr = curr.left
        return curr.val
    aa = root.val       
    if root is None :
        return None 
    
    if root.val > k :
        root.left = delete(root.left,k)
    elif root.val < k :
        root.right = delete(root.right,k)
        
    else :
        if root.left is None :
            return root.right 
        elif root.right is None :
            return root.left 
        else:
            ss = getSucc(root.right)
            root.val = ss 
            root.right = delete(root.right, ss)
            
    return root
            
            
            