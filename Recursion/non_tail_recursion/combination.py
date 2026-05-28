def combination(n,r):
    if r == 0 or r == n:
        return 1
    else:
        return combination(n-1,r-1) + combination(n-1,r)
    
print(combination(4,2))