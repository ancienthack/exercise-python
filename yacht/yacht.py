"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
from typing import Counter, Sized


YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12

def score(dice, category):
    if category == YACHT:
        yacht_unique = []
        for d in dice:
            if d not in yacht_unique:
                yacht_unique.append(d)
        if len(yacht_unique) == 1:
            return 50
    if category == ONES:
        ones_count = 0
        for d in dice:
            if d == 1:
                ones_count += 1
        if ones_count > 0:
            return 1 * ones_count
    if category == TWOS:
        twos_count = 0
        for d in dice:
            if d == 2:
                twos_count += 1
        if twos_count > 0:
            return 2 * twos_count
    if category == THREES:
        threes_count = 0
        for d in dice:
            if d == 3:
                threes_count += 1
        if threes_count > 0:
            return 3 * threes_count
    if category == FOURS:
        fours_count = 0
        for d in dice:
            if d == 4:
                fours_count += 1
        if fours_count > 0:
            return 4 * fours_count
    if category == FIVES:
        fives_count = 0
        for d in dice:
            if d == 5:
                fives_count += 1
        if fives_count > 0:
            return 5 * fives_count
    if category == SIXES:
        sixes_count = 0
        for d in dice:
            if d == 6:
                sixes_count += 1
        if sixes_count > 0:
            return 6 * sixes_count
    if category == FULL_HOUSE:
        # pass
        fh_unique = []
        for d in dice:
            if d not in fh_unique:
                fh_unique.append(d)
        if len(fh_unique) < 3:
            for u in fh_unique:
                fh_count = dice.count(u)
                if fh_count == 3:
                    return sum(dice)
    if category == FOUR_OF_A_KIND:
        # pass
        fk_unique = []
        for d in dice:
            if d not in fk_unique:
                fk_unique.append(d)
        if len(fk_unique) < 3:
            for u in fk_unique:
                fk_count = dice.count(u)
                if fk_count == 4 or fk_count == 5:
                    fk = u
                    return fk*4
    if category == LITTLE_STRAIGHT:
        # pass
        dice.sort()
        if dice == [1, 2, 3, 4, 5]:
            return 30
    if category == BIG_STRAIGHT:
        # pass
        dice.sort()
        if dice == [2, 3, 4, 5, 6]:
            return 30
    if category == CHOICE:
        # pass
        return sum(dice)
    else:
        return 0
