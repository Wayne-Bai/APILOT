import nltk
from nltk.corpus import wordnet as wn

# Ensure that the wordnet data is downloaded
nltk.download('wordnet')

def get_synset_from_sense_key(sense_key):
    """
    Retrieves the synset based on a given sense_key.

    Args:
        sense_key (str): The sense key of a word for which the synset is required.

    Returns:
        synset: The synset corresponding to the given sense key.
    """
    # Get the synset using the sense key
    synsets = wn.synsets('')
    for synset in synsets:
        if any(lemma.key() == sense_key for lemma in synset.lemmas()):
            return synset
    return None

# Example usage
sense_key = "bank.n.01"  # Example sense_key
synset = get_synset_from_sense_key(sense_key)
if synset:
    print("Synset:", synset)
    print("Definition:", synset.definition())
else:
    print("No synset found for the given sense key.")
