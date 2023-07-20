from decimal import Decimal, getcontext

def pow(a, b):
    getcontext().prec = 28

    a = Decimal(a)
    b = Decimal(b)
    result = Decimal(1)

    if b < 0:
        a = Decimal(1) / a
        b = -b

    while b:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2

    return round(float(result), 20)