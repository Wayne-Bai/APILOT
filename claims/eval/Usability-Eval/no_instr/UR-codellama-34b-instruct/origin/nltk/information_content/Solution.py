import nltk
from nltk.corpus import wordnet as wn

def calculate_ic(synset):
    """
    Calculates the Information Content (IC) value of a synset.

    Args:
        synset (wn.Synset): The synset to calculate the IC for.

    Returns:
        float: The IC value of the synset.
    """
    # Get the frequency of the word in the corpus
    freq = synset.corpus_frequency()

    # Calculate the IC using the frequency and the logarithm base 2
    ic = log2(freq)

    return ic
