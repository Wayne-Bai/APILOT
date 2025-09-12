import nltk
from nltk.corpus import wordnet

def get_synset(sense_key):
    try:
        synset = wordnet.synset(sense_key)
        return synset
    except:
        return None

# Example usage:
sense_key = "s.01"
synset = get_synset(sense_key)
if synset:
    print(f"Synset: {synset}")
else:
    print("Synset not found.")
