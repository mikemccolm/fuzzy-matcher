from nltk.corpus import words
import nltk
import random
from typing import Tuple

import sys
sys.path.append('../fuzzy-matcher')
import matching

def getmappings()->dict:
    rows=['qwertyuiop','asdfghjkl','zxcvbnm']
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    mappings = {}
    for letter in alphabet:
        for j in range (0,3):
            if letter in rows[j]:
                row=j
                col=rows[j].index(letter)
                break  
        neighbours = []
        neighbours.append('')
        neighbours.append(str(letter)+str(letter))
        try: 
            if not col == 0:
                neighbours.append(rows[j][col-1])
        except:...
        try: neighbours.append(rows[j][col+1]) 
        except: ...
        if row == 0:
            try: neighbours.append(rows[1][col])
            except:...
            try: 
                if not col == 0:
                    neighbours.append(rows[1][col-1])
            except:...
        elif row == 2:
            try: neighbours.append(rows[1][col])
            except:...
            try: neighbours.append(rows[1][col+1])
            except:...
        elif row == 1:
            try: neighbours.append(rows[0][col])
            except:...
            try: neighbours.append(rows[0][col+1])
            except:...
            try: neighbours.append(rows[2][col])
            except:...
            try: 
                if not col == 0:
                    neighbours.append(rows[2][col-1])
            except:...
        mappings[letter] = neighbours
    return mappings

def scramble_words(words: list[str],mappings:dict, error_rate:float=0.08)->dict[str]:
    typos = {}
    for word in words:
        new_word = ''
        firstLetter = True
        for letter in word:
            x = letter
            if not firstLetter:
                x = random.choice(mappings[letter.lower()]) if random.uniform(0,1) < error_rate else x
            firstLetter = False
            new_word+=x
        if not word==new_word:
            typos[new_word]=word
    return typos

def createTypos()->Tuple[dict[str],list[str]]:
    mappings = getmappings()
    nltk.download('words')
    wordlist = [word.lower() for word in words.words() if ((len(word)>5)and word.isalpha())]
    typos = scramble_words(wordlist,mappings)
    return typos, wordlist

def eval(typos: dict, wordlist: list[str], num_samples: int)->float:
    count = 0
    correct = 0
    for item in typos.items():
        count+=1
        output = matching.match_levenshtein(item[0],wordlist)
        #print('Correct:')
        #print(str(output))
        #print('Typo:')
        #print(str(item[0]))
        #print('Expected: ')
        #print(str(item[1]))
        if (str(output)==str(item[1])):
            print('correct')
            correct+=1
        if count > num_samples:
            print('incorrect')
            break
    print('Accuracy: ' + str(100*(correct/count))+'%')


def main():
    typos,wordlist = createTypos()
    eval(typos, wordlist, 100)

            

if __name__ == "__main__":
    main()