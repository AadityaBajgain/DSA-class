# how to find the greatest common divisor(highest common factor) of two numbers using recursion


def gcd(num1, num2):
    assert num1 == int(num1) and num2 == int(num2), "The number must be integer type"
    num1 = abs(num1)
    num2 = abs(num2)
    if num1 == 0 : return num2
    elif num2 == 0 :return num1
    return gcd(num2, num1 % num2)


print(gcd(-12,1.8))