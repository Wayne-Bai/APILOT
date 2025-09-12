import nltk
from nltk.corpus import wordnet as wn
from math import log

def calculate_ic(synset):
    # Retrieve the definition from the synset
    definition = synset.definition()

    # Count the occurrences of the words in the definition
    word_count = {}
    for word in definition.split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Calculate the Information Content
    total_words = sum(word_count.values())
    ic_values = {}
    for word, count in word_count.items():
        ic_values[word] = log(total_words / count)

    # Return the average Information Content of the words in the definition
    return sum(ic_values.values()) / len(ic_values)

# Test the function
synset = wn.synset('dog.n.01')
print(calculate_ic(synset))
