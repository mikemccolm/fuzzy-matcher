from nltk.corpus import words
import nltk

rows=['qwertyuiop','asdfghjkl','zxcvbnm']
alphabet = 'qwertyuiopasdfghjklzxcvbnm'
mappings = {}
for i in range (len(alphabet)):
    for j in range (0,3):
        if alphabet[i] in rows[j]:
            row=j
            col=rows[j].index(alphabet[i])
            break  
    neighbours = []
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
    mappings[alphabet[i]] = neighbours
         
print(mappings['b'])
#nltk.download('words')
#print (len(words.words()))