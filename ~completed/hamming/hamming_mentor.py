def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Lengths must be the same")
    return sum(1 for char_a, char_b in zip(strand_a, strand_b) if char_a != char_b)


# old solution using map
# def distance(strand_a, strand_b):
#     if len(strand_a) != len(strand_b):
#         raise ValueError("Lengths must be the same")
#     return sum(map(lambda kv: 1 if kv[0] != kv[1] else 0, zip(strand_a, strand_b)))