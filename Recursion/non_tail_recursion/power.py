def pow(m, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return pow(m*m,n/2)
    else:
        return m * pow(m*m, (n-1)/2)
    

print(pow(2,100))


def pow_inefficient(m,n):
    if n == 0:
        return 1
    else:
        return pow(m,n-1) * m
    
print(pow_inefficient(2,100))