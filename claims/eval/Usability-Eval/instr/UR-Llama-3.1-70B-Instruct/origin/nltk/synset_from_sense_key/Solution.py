import nltk
from nltk.corpus import wordnet as wn

# Ensure the wordnet corpus is downloaded
nltk.download('wordnet')

def get_synset(sense_key):
    """
    Retrieves a synset based on a given sense_key.

    Parameters:
    sense_key (str): The sense key for the synset to be retrieved.

    Returns:
    Synset: The synset corresponding to the sense key.
    """
    try:
        # Use the sense key to get the synset
        synset = wn.lemma_from_key(sense_key).synset()
        return synset
    except Exception as e:
        print(f"Error retrieving synset: {e}")
        return None

# Example usage:
sense_key = 'dog.n.01.dog'
synset = get_synset(sense_key)

if synset:
    print(f"Synset: {synset}")
    print(f"Definition: {synset.definition()}")
    print(f"Examples: {synset.examples()}")
