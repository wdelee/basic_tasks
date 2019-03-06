
#input an integer, output binary string of integer

def binary_producer(b):
    import math
    d = [0]

    for k in range(1, b):
        if b % (int(math.pow(2, k))) != b:
            d.append(0)
        else:
            break

    for k in range(0, len(d)):
        if b >= math.pow(2, len(d) - (k + 1)):
            d[k] = 1
            b = b - math.pow(2, len(d) - (k + 1))
    d = ''.join(map(str, d))
    return d
