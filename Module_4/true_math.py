from math import inf


def divide(first, second):
    if int(second) == 0:
        return inf
    return float(first) / float(second)
