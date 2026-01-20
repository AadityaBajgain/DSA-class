# tail factorial implementation 

def tail_factorial(n, base = 1):
    if n < 0:
        return "number must be positive."
    if n <= 1 :
        return base
    
    return tail_factorial(n-1, n * base)

print(tail_factorial(0))