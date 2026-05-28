def e(x,n):
    e.factorial = 1
    e.power = 1
    
    if n == 0:
        return 1
    
    result = e(x,n-1)
    e.factorial *= n
    e.power *= x
    
    return result + (e.power / e.factorial)
    

print(e(3,2))


def taylor(x,n):
    
    result = 1
    for n in range(n,0,-1):
        result = 1 + x/n * result
    
    return result

print(taylor(3,2))


def e_recursion(x,n):
    if not hasattr(e_recursion,"r"):
        e_recursion.r = 1
    if n == 0:
        return e_recursion.r
    else:
        e_recursion.r = 1 + x/n * e_recursion.r
        return e_recursion(x,n-1)
    
print(e_recursion(3,2))