import nltk
from nltk.corpus import wordnet

def get_synset(sense_key):
    synsets = wordnet.synsets(sense_key)
    if synsets:
        return synsets[0]
    else:
        return None

# Example usage:
sense_key = "c02.s01.m01"
synset = get_synset(sense_key)
if synset:
    print(f"Synset: {synset}")
else:
    print("No synset found.")
