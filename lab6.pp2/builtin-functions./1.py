from functools import reduce

def mult(numbers):
    return reduce(lambda x, y: x * y, numbers)
