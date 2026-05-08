# the function is stored in the order and then called in LIFO order

def recursion(n):
    if n < 1:
        print("less than 1")
    else:
        recursion(n-1)
        print(n)
        
recursion(5)

# stack --> in this example its stored in the below order
"""
    recursion(1)
    recursion(2)
    recursion(3)
    recursion(4)
    recursion(5)
"""