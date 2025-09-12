import nltk
from nltk.corpus import wordnet as wn

# Make sure the WordNet data is downloaded:
nltk.download('wordnet')

def get_synset(phrase, sense_key='synonyms'):
    synset = wn.morphy(phrase, pos=wn.VERB)
    return synset

# Example usage:
phrase = "play"
sense_key = get_synset(phrase)
print(synset)
