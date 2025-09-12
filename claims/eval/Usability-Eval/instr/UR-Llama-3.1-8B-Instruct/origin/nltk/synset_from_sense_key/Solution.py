import nltk
from nltk.corpus import wordnet

# Ensure the wordnet corpus is downloaded
nltk.download('wordnet')

# Define a function to retrieve synset based on a given sense_key
def get_synset(word, sense_key):
    synsets = wordnet.synsets(word)
    # Find the synset with the matching sense key
    for synset in synsets:
        for lemma in synset.lemmas():
            if lemma.name() == word and lemma.key() == sense_key:
                return synset

    # If no matching synset is found, return None
    return None

# Test the function
word = input("Enter a word: ")
sense_key = input("Enter a sense_key: ")

synset = get_synset(word, sense_key)

if synset:
    print(f"Synset for '{word}' with sense_key '{sense_key}':")
    print(f"  - Lexicalized Name: {synset.lexname()}")
    print(f"  - Definition: {synset.definition()}")
    print(f"  - Synonyms: {[lemma.name() for lemma in synset.lemmas()]}")
else:
    print(f"No synset found for '{word}' with sense_key '{sense_key}'")
