import nltk
from nltk.corpus import wordnet as wn

def calculate_information_content(synset):
    # Get the frequency of the synset
    frequency = synset.count()
    
    # Get the total number of synsets in the corpus
    total_synsets = len(list(wn.all_synsets()))
    
    # Calculate the probability of the synset
    probability = frequency / total_synsets
    
    # Calculate the Information Content (IC)
    ic = -nltk.log(probability)
    
    return ic

# Example usage
synset = wn.synset('dog.n.01')
ic_value = calculate_information_content(synset)
print(f"Information Content for {synset}: {ic_value}")
