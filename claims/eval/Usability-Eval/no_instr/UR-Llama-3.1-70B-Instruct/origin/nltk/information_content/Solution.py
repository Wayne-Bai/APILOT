# Importing the necessary libraries
import nltk
from nltk.corpus import wordnet

# Ensure the wordnet corpus is downloaded
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Function to calculate the information content of a synset
def calculate_information_content(synset):
    """
    Calculate the information content of a synset.

    The information content is the entropy of the word in the given synset.

    Args:
    - synset (wordnet.Synset): A synset from WordNet.

    Returns:
    - float: The information content of the synset.
    """

    # Get the hypernyms (more general concepts)
    hypernyms = set()

    for lemma in synset.lemmas():
        for syn in lemma.synset().hypernyms():
            hypernyms.add(syn)

    # Calculate the Information Content (IC)
    ic = len(hypernyms) / len(wordnet.all_synsets())

    return ic


# Example usage
if __name__ == "__main__":
    # Define the synset for which we want to calculate the IC
    synset = wordnet.synset('dog.n.01')
    ic = calculate_information_content(synset)
    print(f"The information content of '{synset.lemmas()[0].name()}' is {ic}")
