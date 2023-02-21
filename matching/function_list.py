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

def match_tversky(word,candidates):
    winner = 0
    candidates = [candidate for candidate in candidates if word[0]==candidate[0]]
    for candidate in candidates:
        diff = float(textdistance.tversky.normalized_similarity(candidate.lower(),word.lower()))
        #print(candidate)
        if (diff>winner):
            winner = diff
            match = candidate
    return match

def match_jw(word,candidates):
    winner = 0
    candidates = [candidate for candidate in candidates if word[0]==candidate[0]]
    for candidate in candidates:
        diff = float(textdistance.jaro_winkler.normalized_similarity(candidate.lower(),word.lower()))
        #print(candidate)
        if (diff>winner):
            winner = diff
            match = candidate
    return match
