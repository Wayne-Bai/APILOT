import nltk
from nltk.corpus import wordnet as wn

def get_synset_from_sense_key(sense_key):
    # Split the sense key to extract the lemma and sense number
    lemma, sense_number = sense_key.split('%')
    
    # Retrieve synsets matching the lemma and the sense number
    synsets = wn.synsets(lemma)
    
    for synset in synsets:
        if synset.name().endswith(sense_number):
            return synset
    return None

# Example usage
sense_key = 'dog%1:05:00::'  # Example sense key
synset = get_synset_from_sense_key(sense_key)
print(synset)
