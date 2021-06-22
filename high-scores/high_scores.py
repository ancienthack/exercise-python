def latest(scores):
    return scores[-1]

def personal_best(scores):
    # pb = 0
    # for score in scores:
    #     if score > pb:
    #         pb = score
    # return pb
    return max(scores)

def personal_top_three(scores):
    # top_three = scores
    # if len(scores) > 2:
    #     top_three.sort(reverse=True)
    #     return top_three[0:3]
    # else:
    #     top_three.sort(reverse=True)
    #     return scores
    return sorted(scores, reverse=True)[0:3]
