import sys
sys.path.append('../fuzzy-matcher')
import matching
from nltk.corpus import words
import nltk

def main():
    nltk.download('words')
    wordlist = [word.lower() for word in words.words() if ((len(word)>0)and word.isalpha())]
    while True:
        test_word = input("Enter a word: \n")
        if test_word == 'c':
            break
        else:
            if test_word.lower() in wordlist:
                print("That's a real word, no matching needed.")
            else:
                fixed_word = matching.match_levenshtein(test_word.lower(),wordlist)
                print('Matched to: ' + fixed_word)


if __name__ == "__main__":
    main()