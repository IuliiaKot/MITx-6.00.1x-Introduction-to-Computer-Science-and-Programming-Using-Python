def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    result = ''

    for i in text:
        if (i in string.punctuation or i == ' ' or c.isdigit()):
            result += i
        else:
            result += coder[i]

    return result

