def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    word_text = text.split(' ')
    max_valid = 0
    best_shift = 0

    for shift in range(26):
        num_valid = 0

        for word in word_text:
            p = applyShift(word, shift)
            if isWord(wordList, p):
                num_valid += 1

        if num_valid > max_valid:
            max_valid = num_valid
            best_shift = shift

    return best_shift

