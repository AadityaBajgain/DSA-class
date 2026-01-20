def calculate_factorial(n):
    # it is the form of direct recursion
    if n < 0:
        return "Input number can not be negative"
    if n == 0 or n == 1:  #base case
        return 1
    
    else:
        return n * calculate_factorial(n-1) # recursive call
    


if __name__ == "__main__":
    factorial = calculate_factorial(4)
    if type(factorial) == str:
        print(factorial)
    else:
        print(f"Factorial of the given number is {factorial}")