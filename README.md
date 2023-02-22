# fuzzy-matcher
Playground for experimenting with fuzzy matching techniques

#Setup
pip install -r requirements.txt

##### School Matching
School list in /data
misc/school_matcher matches to school list based on Levenshtein distance
Not used yet, may eventually package and use as multiple inputs in NCAA Predictor

##### Word Matching
The main body of this mini-project.
/matching - functionlist as package with different (Levenshtein distance, Tversky index, Jaro-Winkler similarity) matching algos
/scripts - match_word as cli for matching one word to closest english word
         - match_word_testing containing some artifical typo creation, testing/comparison between algorithms
         
##### Testing
Not implemented yet until this gets used somewhere or expanded on
