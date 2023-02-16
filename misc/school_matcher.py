import textdistance
import gzip
import json

def getlevdistance(schoolname):
    with open('data/schoollist.txt') as f:
        candidates = [line.rstrip('\n') for line in f]
    winner = 999
    for candidate in candidates:
        diff = float(textdistance.levenshtein.normalized_distance(candidate.lower(),schoolname.lower()))
        if (diff<winner):
            winner = diff
            match = candidate
    return match

def driver():
    while True:
        school = input("Enter a poorly spelled school name: \n")
        if school == 'c':
            break
        else:
            outputschool = getlevdistance(school)
            print('Matched to: ' + outputschool)



if __name__ == "__main__":
    driver()
