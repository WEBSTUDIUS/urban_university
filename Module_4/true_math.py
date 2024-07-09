from math import inf


def divide(first, second):
    if float(second) == 0.0:
        return inf
    return float(first) / float(second)
