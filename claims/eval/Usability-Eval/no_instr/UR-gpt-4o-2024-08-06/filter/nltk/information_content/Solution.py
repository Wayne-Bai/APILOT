import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic

# Ensure you have downloaded the necessary data
nltk.download('wordnet')
nltk.download('wordnet_ic')
nltk.download('omw-1.4')

def calculate_information_content(synset, ic_corpus='ic-brown.dat'):
    # Select the correct information content corpus from the wordnet_ic package
    ic = wordnet_ic.ic(ic_corpus)

    # Calculate and return the information content of the synset
    return synset.information_content(ic)

# Example usage
synset = wn.synset('dog.n.01')
ic_value = calculate_information_content(synset)
print(f'The Information Content value for {synset.name()} is {ic_value}')
