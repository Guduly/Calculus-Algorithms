# func1 * 'func2 + 'func1 * func2#
def productRule(base2, exponent2, exponent1, base1, var1):
    
    ## First step
    print("Formula: func1 * 'func2 + 'func1 * func2/n")

    return print(f"{(base1)(base2 * exponent2)}{var1}^{exponent1+(exponent2-1)} + {(base2)(base1 * exponent1)}{var1}^{exponent2+(exponent1-1)}")

productRule(base2=2,exponent2=3,exponent1=2,base1=3,var1='x')


