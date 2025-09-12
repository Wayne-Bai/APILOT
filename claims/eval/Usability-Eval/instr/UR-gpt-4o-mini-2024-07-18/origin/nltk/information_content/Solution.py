import nltk
from nltk.corpus import wordnet as wn

def calculate_information_content(synset_name):
    synset = wn.synset(synset_name)
    frequency = synset.lemmas()[0].count()  # Get the frequency of the first lemma
    total_frequency = sum(lemma.count() for lemma in synset.lemmas())  # Sum of frequencies for all lemmas in the synset
    
    if total_frequency > 0:
        information_content = -1 * (frequency / total_frequency).log()  # Calculate IC
    else:
        information_content = 0  # Default value if there is no frequency information

    return information_content

# Example usage
print(calculate_information_content('dog.n.01'))  # Replace with the desired synset
