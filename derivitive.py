def differciation(exponent, base, var):
    ''' >>> differciation(2,5)
    10X^1 
        >>> differciation(23,52)
    1196X^22 
        >>> differciation(10,6)
    60X^9 '''
    return print(f"{base * exponent}{var}^{exponent-1}")

differciation(23,52, var='x')
differciation(10,6,var='x')