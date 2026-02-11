LOW = 1
HIGH = 64

def square(number):
    if number < LOW or number > HIGH:
        raise ValueError("square must be between 1 and 64")
    else:
        return 2 ** (number - 1)


def total():
    return 2 ** HIGH - 1