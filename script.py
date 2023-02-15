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

fname = "github-typo-corpus.v1.0.0.jsonl.gz"

with gzip.open(fname,'r') as fin:  
    json_list = list(fin)

for json_str in json_list:
    result = json.loads(json_str)
    print(result['edits'][0]['src']['text'])
    print(result['edits'][1]['src']['text'])
    break

while False:
    school = input("Enter a poorly spelled school name: \n")
    if school == 'c':
        break
    else:
        outputschool = getlevdistance(school)
        print('Matched to: ' + outputschool)



