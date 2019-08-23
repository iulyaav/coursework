import math

def digits(x):
    if x > 0:
        return int(math.log10(x)) + 1
    elif x == 0:
        return 1
    else:
        return int(math.log10(-n)) + 2

def karatsuba(a, b, d):
    """
    Some comments here
    """
    if d == 2:
        return a * b
    d = d // 2

    a_1 = a // (10 ** d)
    a_2 = a % (10 ** d)

    b_1 = b // (10 ** d)
    b_2 = b % (10 ** d)

    x = karatsuba(a_1, b_1, d)
    y = karatsuba(a_2, b_2, d)
    z = karatsuba(a_1 + a_2, b_1 + b_2, d) - x - y
    return x * (10**(d*2)) + z * (10 ** d) + y


if __name__ == "__main__":
    first_number, second_number = [int(x) for x in input().split(' ')]
    if digits(first_number) != digits(second_number):
        print("We are not supporting numbers of different lengths at the moment")
    else:
        print(karatsuba(first_number, second_number, digits(first_number)))

