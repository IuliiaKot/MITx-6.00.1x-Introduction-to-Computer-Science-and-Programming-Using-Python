def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    res = ''
    if s1 == '':
        res = s2
    elif s2 == '':
        res = s1
    elif s1 == '' and s2 == '':
        res =  ''
    else:
        if len(s1) > len(s2):
            a = s2
            b = s1
        else:
            a = s1
            b = s2
        for i in range(len(a)):
            res += s1[i] + s2[i]  
        if (len(s1) != len(s2)):
            res += b[len(a):]            
    return res
