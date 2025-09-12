import nltk

# Downloading necessary resources
nltk.download('wordnet')

from nltk.corpus import wordnet as wn

def calculate_info_content(name):
    synsets = wn.synsets(name)
    if not synsets:
        raise ValueError(f"No synsets found for the word '{name}'")

    print("Synsets:", synsets)

    total_entropy = 0
    for synset in synsets:
        pos = synset.pos()
        print(f"Synset position: {pos}")

        if pos == 'n':
            total_entropy += synset.path_length(synset)

    return total_entropy / len(synsets)

# Example usage
word = "tree"
print(f"Information Content for '{word}':", calculate_info_content(word))
