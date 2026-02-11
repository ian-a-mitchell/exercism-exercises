LOW = 0
HIGH = 65

def square(number):
    if not (number > LOW and number < HIGH):
        raise ValueError("square must be between 1 and 64")
    else:
        return 2 ** (number - 1)


def total():
    # The partial sum of powers of 2^k from k = 0 to k = n is provably
    # 2^(n + 1) - 1
    # Per problem definition, square 1 has 1 grain on it, square 2 has 2,
    # and so on, meaning that the correct exponent is 1 less than the square
    # number (as shown in the function "square").
    # Therefore the sum of powers of two from square 1 to square 64
    # is the sum of powers of 2^k from k = 0 to k = 63: 2^64 - 1
    return 2 ** (HIGH - 1) - 1