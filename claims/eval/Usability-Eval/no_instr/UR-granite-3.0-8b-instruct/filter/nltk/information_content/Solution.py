import nltk
from nltk.corpus import wordnet

def calculate_info_content(synset):
    """
    Calculate the Information Content value for a synset.

    Parameters:
    synset (wordnet.Synset): A synset from the WordNet lexical database.

    Returns:
    float: The Information Content value for the given synset.
    """
    # Get the frequency of the synset in the corpus
    freq = synset.count()

    # Get the total number of synsets in the corpus
    total_synsets = sum(s.count() for s in wordnet.all_synsets())

    # Calculate the Information Content value
    info_content = -((freq / total_synsets) * nltk.corpus.brown.log_prob(synset.lemma_names()))

    return info_content

# Example usage:
synset = wordnet.synset('dog.n.01')
info_content = calculate_info_content(synset)
print(f"The Information Content value for the synset '{synset.lemma_names()}' is: {info_content}")
