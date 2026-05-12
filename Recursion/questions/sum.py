# how to find the sum of the positive integers using recursion ?


def sum_of_digit(n):
    
    if n < 0 or type(n) != int:
        return "Must be integer type greater than 0"
    if n == 0:
        return 0 
    return int(n%10) + sum_of_digit(int(n//10))
print(sum_of_digit(1895))