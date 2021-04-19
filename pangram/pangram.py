import string 

def is_pangram(sentence: str) -> bool:
    '''Every letter in a sentence should be [a-z] at least onece otherwhise return False.'''
    sentence = sentence.lower()

    # finding letter by letter in the word and return fase if any missing     
    return all(letter in sentence for letter in string.ascii_lowercase)
