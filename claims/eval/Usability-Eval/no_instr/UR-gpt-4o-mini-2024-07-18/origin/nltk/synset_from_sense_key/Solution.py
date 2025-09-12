import nltk
from nltk.corpus import wordnet as wn

def get_synset_by_sense_key(sense_key):
    # Use the sense_key to retrieve the synset
    synset = wn.synset_from_sense_key(sense_key)
    return synset

# Example usage:
# Replace 'your_sense_key' with an actual sense key you want to retrieve
# sense_key = 'your_sense_key'
# synset = get_synset_by_sense_key(sense_key)
# print(synset)
