def pow(a, b): 
    result = 1
    if b < 0:
        a = 1/ a
        b = abs(b)     
    for i in range(b): 
        result = result * a         
    return round(result, 20)  # Round to 20 decimal places