from string import ascii_lowercase

def is_pangram(sentence):
    # if ascii_lowercase in sentence.lower():
    #     return True
    # else:
    #     return False
    # count = 0
    # for i in range(len(ascii_lowercase)):
    #     if ascii.lower[i] in sentence.lower():
    #         count += 1
    count = len([i for i in range(len(ascii_lowercase)) if ascii_lowercase[i] in sentence.lower()])
    if count == 26:
        return True
    else:
        return False
