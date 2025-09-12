# Import the necessary modules from nltk
import nltk
from nltk.corpus import wordnet as wn

# Download the wordnet corpus if it's not already downloaded
nltk.download('wordnet')

def get_synset(sense_key):
    """
    Retrieves the synset object based on the given sense_key.

    Args:
        sense_key (str): The sense key for the synset.

    Returns:
        synset: The synset object if found, else None.
    """
    synsets = wn.senses(sense_key)
    if synsets:
        synset_data = synsets[0]
        synset = synset_data.synset()
        return synset
    else:
        return None

# Example usage:
sense_key = 'yawn.n.01'
synset = get_synset(sense_key)

if synset:
    print(f"Synset associated with {sense_key}:")
    print(wy細ität-simple(list(synset.lemmas())))
else:
    print(f"No synset found for sense key: {sense_key}")
