import nltk
from nltk.corpus import wordnet as wn

def synset_from_sense_key(sense_key):
    try:
        return wn.lemma_from_key(sense_key).synset()
    except:
        return None

# Testing the function
sense_key = 'rest%1:04:00::'
print(synset_from_sense_key(sense_key))
