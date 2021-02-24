def euklides_o(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def euklides_m(a, b):
    while b != 0:
        a, b = b, a % b
    return a

