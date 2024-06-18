# pascal triangle element 


def nCr (n, r) :
    res = 1
    for i in range(r) :
        res = res*(n-i)
        res= res/(i+1)     
    return int(res)

    
def pascal_triangle_element(row,col) :
    return nCr(row-1,col-1)
    
    
pascal_triangle_element(6,3)



def pascalRowValues(n):
    
    ans= []
    res = 1 
    
    for i in range(n+1) :
        ans.append(int(res))
        res= res*(n-i)
        res= res/(i+1)
       
    return ans 

pascalRowValues(5)




def print_pascal_triangle(n) :
    
    for i in range(n) :
        print(pascalRowValues(i)) 
        
        
        
print_pascal_triangle(6)