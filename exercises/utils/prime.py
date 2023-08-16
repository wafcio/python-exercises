import math

def is_prime(number):
    square_root = int(math.sqrt(number))

    for factor in range(2, square_root+1):
        if number % factor == 0:
            return False

    return True
