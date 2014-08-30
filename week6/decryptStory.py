def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    ### TODO
    text = getStoryString()
    word_list = loadWords()
    shift = findBestShift(word_list, text)
    return applyShift(text, shift)
