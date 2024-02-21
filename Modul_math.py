import math
#
# print(math.pi)
# print(math.e)
# print(math.sqrt(100)) # sqrt is square root of a number
# print(math.log(100)) #
# print(math.factorial(10)) #factorial is - 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 *...

def calc_factorial(num):
    if type(num) is not int:
        raise TypeError("calc_factorial only accepts integer values")
    if num <= 0:
        raise ValueError("calc_factorial only accepts positive integer values")
    if num == 1:
        return calc_factorial(num - 1) * num
        return num
# or -->
    result = 1
    i = num
    while i > 0:
        result *= i
        i -= 1
    return result

print(calc_factorial(10)) # or... see next line.
print(math.factorial(10))

