import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Ensure the wordnet corpus is downloaded
nltk.download('wordnet')

def calc_information_content(word):
    """
    Calculate the Information Content (IC) of a word.

    The IC is the inverse logarithm of the frequency of the word in WordNet.

    Parameters:
    - word: A word for which to calculate the IC.

    Returns:
    - The IC of the word.
    """
    # Get all synsets for the word
    synsets = wordnet.synsets(word)

    # If there are no synsets, return None
    if not synsets:
        return None

    # Initialize an empty set to store the IC values
    ic_values = set()

    # For each synset, add its semantic field to the set
    for synset in synsets:
        # Get the words in the POS tag (lemma_names)
        for lemma_name in synset.lemmas():
            if lemma_name.name() == word:
                # Calculate the IC of the semantic field
                ic = 1 / synset.lexname().count('.')
                ic_values.add(ic)

    # Calculate the mean IC
    # If there is no IC value, return None
    if not ic_values:
        return None
    mean_ic = sum(ic_values) / len(ic_values)

    return mean_ic


# Test the function
word = input("Enter a word: ")
ic = calc_information_content(word)
if ic is not None:
    print(f"The Information Content of '{word}' is {ic}")
else:
    print(f"No Information Content could be calculated for '{word}'")

