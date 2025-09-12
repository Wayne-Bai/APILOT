import nltk
from nltk.corpus import wordnet as wn

def get_synset_by_sense_key(sense_key):
    try:
        sense = wn._sense_from_key(sense_key)
        if sense is not None:
            return sense.synset()
        else:
            print(f"No synset found for sense_key: {sense_key}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
sense_key = 'fact%1:06:00::'
synset = get_synset_by_sense_key(sense_key)
if synset is not None:
    print(f"Synset: {synset}")
