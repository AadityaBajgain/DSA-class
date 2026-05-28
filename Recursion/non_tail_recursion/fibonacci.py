def calculate_fibonacci(n):
    if n < 0:
        return "Input number can not be negative"
    # base cases
    if n == 0: 
        return 0
    if n == 1:
        return 1
    # general cases
    return calculate_fibonacci(n-2)+calculate_fibonacci(n-1)

print(f"fifth fibonacci number is {calculate_fibonacci(5)}")



# this is the function with memoization that reduces the time complexity of the above function from O(2^n) to O(n)

f = [-1] * 10
def fib(n):
    if n < 0:
        return "the input number can not be negative"
    if n<=1:
        f[n] = n
        return n
    else:
        if f[n-2] == -1:
            f[n-2] = fib(n-2)
        if f[n-1] == -1:
            f[n-1] = fib(n-1)
        return f[n-2] + f[n-1]
    
print(fib(5))