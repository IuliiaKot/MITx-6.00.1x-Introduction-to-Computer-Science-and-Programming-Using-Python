def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    a = b
    i = 1
    if x < b:
        return 0
    while a*b <= x:
        if b == 0:
            return 0
        i+=1
        a*= b
    return i
