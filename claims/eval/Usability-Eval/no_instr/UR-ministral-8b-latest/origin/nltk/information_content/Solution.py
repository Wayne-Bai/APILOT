import nltk
from nltk.corpus import wordnet

# Ensure you have the necessary NLTK data files downloaded
# nltk.download('wordnet')

def calculate_information_content(synset):
    """
    Calculate the Information Content for a WordNet synset.

    Args:
        synset (nltk.corpus.wordnet.synset): A WordNet synset.

    Returns:
        float: The information content of the synset.
    """
    # Get the probability of the synset
    P_synset = synset.prob()

    # Calculate information content using the formula -log2(P_synset)
    info_content = -nltk.math.log(P_synset, 2)

    return info_content

# Example usage
example_synset = wordnet.synsets('dog')[0]
content = calculate_information_content(example_synset)
print(f"Information Content of the synset for 'dog': {content}")
