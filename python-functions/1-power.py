import math


def pow(a, b):
    result = 1

    if b < 0:
        a = 1 / a
        b = -b

    while b:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2

    return result


def test_pow():
    assert math.isclose(pow(10, -2), 0.01, rel_tol=1e-9)
    assert math.isclose(pow(-98, -10), 1.223881142011411e-20, rel_tol=1e-9)


test_pow()
