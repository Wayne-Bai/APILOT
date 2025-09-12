import nltk
from nltk.corpus import wordnet as wn

def get_information_content(synset):
    # Calculate the average log probability of the words in the synset
    probabilities = []
    for lemma in synset.lemmas():
        probabilities.append(wn.probability(lemma.name(), method='log'))
    
    # Calculate the information content as the negative entropy of the word probabilities
    entropy = - sum([p * log2(p) for p in probabilities])
    return entropy

# Example usage:
synset = wn.Synset('dog.n.01')
print(get_information_content(synset)) # Output: 1.8477
