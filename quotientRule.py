def quotientRule(base2, exponent2, exponent1, base1, var1):
    
    ## First step
    print("Formula: 'func1 * func2 - func1 * 'func2)/func2^2")
    
    return print(f"({(base1*exponent1)}{var1}^{exponent1-1})({base2}{var1}^{exponent2}) - ({base1}{var1}^{exponent1})({(base2*exponent2)}{var1}^{exponent2-1}) / ({base2}{var1}^{exponent2})^2")

## Units tests
quotientRule(base2=2,exponent2=3,exponent1=2,base1=3,var1='x')
'''
-->Formula: 'func1 * func2 - func1 * 'func2)/func2^2
(6x^1)(2x^3) - (3x^2)(6x^2) / (2x^3)^2
'''
quotientRule(base2=4,exponent2=5,exponent1=1,base1=4,var1='Y')
'''
-->Formula: 'func1 * func2 - func1 * 'func2)/func2^2
(4Y^0)(4Y^5) - (4Y^1)(20Y^4) / (4Y^5)^2
'''
quotientRule(base2=9,exponent2=3,exponent1=6,base1=465,var1='Y')
'''
--> Formula: 'func1 * func2 - func1 * 'func2)/func2^2
(2790Y^5)(9Y^3) - (465Y^6)(27Y^2) / (9Y^3)^2
'''