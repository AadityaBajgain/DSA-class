# how to convert decimal to binary using recursion?

def decimal_to_binary(n):
    assert n == int(n), "The number must be integer type"
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimal_to_binary(int(n/2))
    
    
print(decimal_to_binary(12))
    