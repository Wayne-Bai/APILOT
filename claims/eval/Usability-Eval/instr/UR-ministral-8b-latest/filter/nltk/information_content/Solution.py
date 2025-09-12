import nltk
from nltk.corpus import wordnet as wn

def calculate_information_content(synset):
    # Calculate the Information Content value for a synset
    total_word_count = sum(wn.synsets(word)[0].pos_counts["total"] for word in synset.lemmas())

    # The Information Content value is calculated as the total number of words in the synset
    information_content = len(synset.lemmas())

    return information_content

# Example usage:
synset = wn.synsets('happiness')[0]
ic_value = calculate_information_content(synset)
print(f"Information Content for synset '{synset}' is {ic_value}")
