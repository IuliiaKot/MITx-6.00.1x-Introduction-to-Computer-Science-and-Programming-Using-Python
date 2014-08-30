def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 
    dt = {}
    for i in range(len(string.ascii_lowercase)):
        s = (i + shift)  % 26
        c = string.ascii_lowercase[i]
        a = string.ascii_lowercase[s]
        dt[c] = a
        dt[c.upper()] = a.upper()
 
    return dt

