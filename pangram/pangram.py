import string 

def is_pangram(sentence):
    '''Every letter in a sentence should be [a-z] at least onece otherwhise return False.'''
    sentence = sentence.lower()

    # finding letter by letter in the word and return fase if any missing     
    for c in string.ascii_lowercase:
        if c not in sentence: 
            return False
    return True

