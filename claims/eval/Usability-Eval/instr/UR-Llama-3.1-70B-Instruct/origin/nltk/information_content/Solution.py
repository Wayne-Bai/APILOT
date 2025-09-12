import nltk
from nltk.corpus import wordnet
from math import log

# Ensure the wordnet corpus is downloaded
nltk.download('wordnet')

def calculate_information_content(synset):
    """
    Calculate the Information Content value for a synset.

    The Information Content of a concept is estimated as the negative log likelihood 
    of encountering an instance of that concept, which can be approximated using the 
    Resnik measure.

    :param synset: The synset for which to calculate the Information Content value
    :return: The Information Content value of the given synset
    """
    # Calculate the frequency of the synset
    freq = len(wordnet.synsets(synset.pos(), synset.name().split('.')[0]))

    # Calculate the total number of synsets
    total_synsets = len(list(wordnet.all_synsets(synset.pos())))

    # Calculate the Information Content value
    ic = -log(freq / total_synsets)

    return ic

# Example usage
dog_synset = wordnet.synset('dog.n.01')
ic_value = calculate_information_content(dog_synset)
print(f"The Information Content value for {dog_synset} is {ic_value}")
