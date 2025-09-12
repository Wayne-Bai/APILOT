import nltk
from nltk.corpus import wordnet

# Ensure the wordnet corpus is downloaded
nltk.download('wordnet')

def get_synset(sense_key):
    """
    Retrieves the synset based on a given sense_key.
    
    Args:
    sense_key (str): The sense key for the synset.
    
    Returns:
    Synset: The synset corresponding to the sense_key, or None if not found.
    """
    return wordnet._synset_from_pos_and_offset(*sense_key.split('%')[1:3])

# Example usage:
sense_key = "dog%1:08:00::"
synset = get_synset(sense_key)

if synset:
    print(synset)
    print("Offsets: ", synset.offset())
    print("POS: ", synset.pos())
    print("Name: ", synset.name())
    print("Lemmas: ", [lemma.name() for lemma in synset.lemmas()])
else:
    print("No synset found for the given sense_key")
