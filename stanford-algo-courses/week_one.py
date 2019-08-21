import math

def digits(x):
    if x > 0:
        return int(math.log10(x)) + 1
    elif x == 0:
        return 1
    else:
        return int(math.log10(-n)) + 2

def karatsuba(a, b):
    """
    Some comments here
    """
    if digits(a) == 1 and digits(b) == 1:
        return a * b

    a_1 = a // (10 ** digits(a))
    a_2 = a % (10 ** digits(a))

    b_1 = b // (10 ** digits(b))
    b_2 = b % (10 ** digits(b))



if __name__ == "__main__":
    first_number, second_number = [int(x) for x in input().split(' ')]
    print(karatsuba(first_number, second_number))
