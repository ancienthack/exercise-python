def distance(strand_a, strand_b):
    err = 0
    if len(strand_a) == len(strand_b):
        return len([i for i in range(len(strand_a)) if strand_a[i] != strand_b[i]])
    else:
        raise ValueError('Strands of differing lengths.')
