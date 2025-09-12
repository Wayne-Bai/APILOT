
import nltk
from nltk.corpus import wordnet as wn

def get_synset(sense_key):
    """Retrieves the synset corresponding to the given sense key"""
    synset = None
    for i in range(wn.synset_count()):
        if wn.synsets[i].lemma == sense_key:
            synset = wn.synsets[i]
            break
    return synset
