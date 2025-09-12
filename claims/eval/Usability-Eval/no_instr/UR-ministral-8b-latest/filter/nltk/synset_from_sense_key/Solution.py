import nltk

# Ensure you have downloaded the necessary NLTK data
nltk.download('wordnet')

from nltk.corpus import wordnet as wn

# Function to retrieve synset based on a given sense_key
def get_synset(sense_key):
    synset = wn.synsets('dummy')[int(sense_key) - 1]  # 'dummy' word is used as a placeholder to validate sense_key
    return synset

# Example usage
sense_key = 1  # Sense key to retrieve
synset = get_synset(sense_key)
print(synset)
