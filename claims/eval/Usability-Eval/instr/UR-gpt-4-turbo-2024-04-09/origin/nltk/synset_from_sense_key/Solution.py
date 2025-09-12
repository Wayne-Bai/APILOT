import nltk
from nltk.corpus import wordnet as wn

def get_synset_from_sense_key(sense_key):
    # Ensure that the wordnet corpus is downloaded
    nltk.download('wordnet')
    
    # Get the synset based on the sense key
    synset = wn.lemma_from_key(sense_key).synset()
    return synset

# Example usage
sense_key = 'bank%1:06:00::'  # sense key for a particular meaning of "bank"
synset = get_synset_from_sense_key(sense_key)
print(synset)
