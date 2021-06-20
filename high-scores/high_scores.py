def latest(scores):
    return scores.pop()

def personal_best(scores):
    pb = 0
    for score in scores:
        if score > pb:
            pb = score
    return pb

def personal_top_three(scores):
    top_three = []
    if len(scores) > 2:
        # for score in scores:
        #     top_three.sort()
        #     while len(top_three) < 3:
        #         top_three.append(score)
        #     if score > top_three[0]:
        #         top_three.pop(0)
        #         top_three.append(score)
        scores.sort()
        while len(top_three) < 3:
            top_three.append(scores.pop(-1))
        top_three.sort(reverse=True)
        return top_three
    else:
        scores.sort(reverse=True)
        return scores
