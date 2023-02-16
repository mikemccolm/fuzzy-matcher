import textdistance

def match_levenshtein(word,candidates):
    winner = 999
    candidates = [candidate for candidate in candidates if word[0]==candidate[0]]
    for candidate in candidates:
        diff = float(textdistance.levenshtein.normalized_distance(candidate.lower(),word.lower()))
        #print(candidate)
        if (diff<winner):
            winner = diff
            match = candidate
    return match
