def pow(a, b):
    # Handle special cases
    if b == 0:
        return 1
    elif b < 0:
        return 1 / pow(a, -b)
    
    # Recursive calculation for positive powers
    result = 1
    for _ in range(b):
        result *= a
    return result