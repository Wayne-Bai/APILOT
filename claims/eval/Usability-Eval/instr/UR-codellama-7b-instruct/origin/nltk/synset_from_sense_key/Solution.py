
from nltk.corpus import wordnet as wn

def retrieve_synset(sense_key):
    synsets = wn.synsets()
    for synset in synsets:
        if sense_key in synset.sense_keys():
            return synset
