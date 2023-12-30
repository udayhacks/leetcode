def match(a, b):
    if ( ( a== '(' and b ==')') or (a=='[' and b ==']') or ( a== '{' and b =='}') ) :
        return True
    return False

def parenthesis(s):
    stack = []
    for i in s :
        if i in ('(' ,'{','[') :
            stack.append(i)
        else :
            #if string starting with the ending brackets 
            if not stack :
                return False 
            elif match(stack[-1],i) == False:
                return False 
            else:
                stack.pop()
#if stack contain exta opening brackets         
    if stack :
        return False
    return True



                
s = "()[]{}"
l = parenthesis(s)
print(l)