import nltk
from nltk.corpus import wordnet

def calculate_information_content(synset):
    # Get the frequency of the synset in the corpus
    frequency = synset.count()

    # Get the total number of synsets in the corpus
    total_synsets = len(wordnet.all_synsets())

    # Calculate the information content using the formula:
    # IC = -log2(P(synset))
    # where P(synset) is the probability of the synset, which is the frequency of the synset divided by the total number of synsets
    information_content = - nltk.probability.log2(frequency / total_synsets)

    return information_content

# Example usage:
synset = wordnet.synset('person.n.01')
information_content = calculate_information_content(synset)
print(f"The information content of the synset '{synset.lemmas()[0].name()}' is: {information_content}")
