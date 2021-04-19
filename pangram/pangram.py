def is_pangram(sentence):
    '''Every letter in a sentence should be [a-z] at least onece otherwhise return False.'''
    alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    # finding letter by letter in the word and return fase if any missing
    for c in alphabet:
        if c not in sentence.lower(): return False
    return True
