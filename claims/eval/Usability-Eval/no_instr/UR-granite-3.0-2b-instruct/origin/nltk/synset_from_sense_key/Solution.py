import nltk
from nltk.corpus import wordnet

def retrieve_synset(sense_key):
    synsets = wordnet.synsets(sense_key)
    if synsets:
        return synsets[0]
    else:
        return None
