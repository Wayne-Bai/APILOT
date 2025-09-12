import nltk
from nltk.corpus import wordnet as wn

# Ensure the wordnet corpus is downloaded
nltk.data.path.append(nltk.data.find('corpora'))

def retrieve_synset(sense_key):
    synset = wn.synset(sense_key)
    return synset

# Example usage
sense_key = 'dog.n.01'  # Example sense_key for the word 'dog'
synset = retrieve_synset(sense_key)
print(synset)
