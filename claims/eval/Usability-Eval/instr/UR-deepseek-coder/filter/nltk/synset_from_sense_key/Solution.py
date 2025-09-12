import nltk
from nltk.corpus import wordnet as wn

def synset_from_sense_key(sense_key):
    lemma = sense_key.split('%')[0]
    pos = sense_key.split('%')[1][0]
    synsets = wn.synsets(lemma, pos=pos)
    for synset in synsets:
        for lemma in synset.lemmas():
            if lemma.key() == sense_key:
                return synset
    return None

# Example usage:
sense_key = "dog%1:06:00::"
synset = synset_from_sense_key(sense_key)
if synset:
    print(f"Synset found: {synset}")
else:
    print("Synset not found.")
