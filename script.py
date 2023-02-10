import editdistance

def getlevdistance(schoolname):
    with open('data/schoollist.txt') as f:
        candidates = [line.rstrip('\n') for line in f]
    winner = 999
    for candidate in candidates:
        diff = int(editdistance.eval(candidate.lower(),schoolname.lower()))
        if (diff<winner):
            winner = editdistance.eval(candidate,schoolname)
            match = candidate
    return match


while True:
    school = input("Enter a poorly spelled school name: \n")
    if school == 'c':
        break
    else:
        outputschool = getlevdistance(school)
        print('Matched to: ' + outputschool)



