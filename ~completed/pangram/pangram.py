from string import ascii_lowercase

def is_pangram(sentence):
    count = len([i for i in range(len(ascii_lowercase)) if ascii_lowercase[i] in sentence.lower()])
    if count == 26:
        return True
    else:
        return False
