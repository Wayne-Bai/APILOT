import nltk
from nltk.corpus import wordnet as wn

def get_synset_from_sense_key(sense_key):
    # Obtain the synset using lemma from sense key
    lemma = wn.lemma_from_key(sense_key)
    return lemma.synset()

# Example usage
sense_key = 'bank%1:17:00::'
synset = get_synset_from_sense_key(sense_key)
print(f"The synset for sense key {sense_key} is {synset}")
