# power of number using recursion

def power(num,pow):
    assert int(pow) == pow, "exponent must me integer type only"
    if pow == 0:
        return 1
    if pow < 0:
        return 1 / (num * power(num,abs(pow) - 1))
    return num * power(num,pow - 1)

print(power(4,-1))