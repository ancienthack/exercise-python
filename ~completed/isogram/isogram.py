from string import ascii_lowercase

def is_isogram(string):
    for i in ascii_lowercase:
        if string.lower().count(i) > 1:
            return False
    return True        
