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