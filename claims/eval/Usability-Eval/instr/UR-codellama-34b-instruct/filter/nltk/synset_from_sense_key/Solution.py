import nltk
from nltk.corpus import wordnet as wn

def get_synset_by_sense_key(sense_key):
    """Retrieves synset based on a given sense key"""
    # Parse the sense key to get the lemma and sense number
    lemma, sensenum = sense_key.split('.')
    # Get the synset for the lemma and sense number
    synset = wn.synset(lemma, int(sensenum))
    return synset
