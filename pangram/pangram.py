def is_pangram(sentence):
    """Every letter in a sentence should be [a-z] at least onece otherwhise return False."""
    c = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    phraseLetters = ""
    for char in sentence.lower():
        for letter in alphabet:
            if char == letter and char not in phraseLetters:
                phraseLetters += char
    for char in phraseLetters:
        for letter in alphabet:
            if char == letter:
                c += 1
    if c == 26:
        return True
    else:
        return False
