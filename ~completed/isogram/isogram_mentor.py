# adapted from mjiggidy's solution
# https://exercism.io/tracks/python/exercises/isogram/solutions/3637f46dc8114f25807af140eaa5df03

def is_isogram(test_string):
    caseless_string = [char.casefold()
                       for char in test_string if char.isalpha()]
    return len(caseless_string) == len(set(caseless_string))


# # old more verbose solution
# from itertools import groupby

# def is_isogram(string):
#     return all(len(list(char_list)) == 1 for char, char_list in groupby(sorted(
#         char for char in [char for char in string.lower()] if char.isalpha())))