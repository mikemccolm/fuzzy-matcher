from nltk.corpus import words
import nltk
import random
from typing import Tuple
import random
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

def createTypos(error_rate:float=0.08)->Tuple[dict[str],list[str]]:
    mappings = getmappings()
    nltk.download('words')
    wordlist = [word.lower() for word in words.words() if ((len(word)>5)and word.isalpha())]
    typos = scramble_words(wordlist,mappings, error_rate)
    return typos, wordlist

def rearrangeDictionary(typos: dict, seed:int=1)->dict[str]:
    l = list(typos.items())
    random.Random(seed).shuffle(l)
    d_shuffled = dict(l)
    return d_shuffled

def getmatches(typos: dict, wordlist: list[str], num_samples: int, lev: bool=True, tve: bool=True, jw: bool=True)->list[str]:
    results = []
    count = 0
    for item in typos.items():
        count +=1
        record = {"original":item[0], "expected":item[1]}
        #include levenshtein distance
        if lev:
            lev_output = matching.match_levenshtein(record['original'],wordlist)
        else:
            lev_output = None
        record['predicted_lev'] = lev_output

        #include tversky index
        if tve:
            tve_output = matching.match_tversky(record['original'],wordlist)
        else:
            tve_output = None
        record['predicted_tve'] = tve_output

        #include jaro-winkler similarity
        if jw:
            jw_output = matching.match_jw(record['original'],wordlist)
        else:
            jw_output = None
        record['predicted_jw'] = jw_output
        
        results.append(record)
        if count >= num_samples:
            break
    return results

def eval(results):
    if results:
        active_lev = True if results[0]['predicted_lev'] is not None else False
        active_jw = True if results[0]['predicted_jw'] is not None else False
        active_tve = True if results[0]['predicted_tve'] is not None else False
        if active_lev:
            lev_correct = [x for x in results if x['predicted_lev']==x['expected']]
            print('Levenshtein Accuracy: ' + str(100*(len(lev_correct)/len(results)))+'%')
        if active_jw:
            jw_correct = [x for x in results if x['predicted_jw']==x['expected']]
            print('Jaro-Winkler Accuracy: ' + str(100*(len(jw_correct)/len(results)))+'%')
        if active_tve:
            tve_correct = [x for x in results if x['predicted_tve']==x['expected']]
            print('Tversky Accuracy: ' + str(100*(len(tve_correct)/len(results)))+'%')
        return
    else:
        print('No predictions were made.')
    
def main():
    typos,wordlist = createTypos(0.1)
    typos = rearrangeDictionary(typos,random.randint(0,999999))
    preds = getmatches(typos, wordlist, 25)
    eval(preds)

            

if __name__ == "__main__":
    main()
