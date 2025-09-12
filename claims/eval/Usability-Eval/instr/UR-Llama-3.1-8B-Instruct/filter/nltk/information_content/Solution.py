import nltk
from nltk.corpus import wordnet

#Ensure the wordnet corpus is downloaded
nltk.download('wordnet')

def calculate_ic(synset):
    """
    Calculate the Information Content (IC) of a synset
    IC is the negative log value of the probability of synset given the word.
    """
    # Get hyponyms and hypernyms of the synset
    hyponyms = synset.hyponyms()
    hypernyms = synset.hypernyms()
    
    # Initialize count of hyponyms and hypernyms
    count_hyponyms = 0
    count_hypernyms = 0
    
    # Count the number of hyponyms and hypernyms
    for hyponym in hyponyms:
        count_hyponyms += len(hyponym.hyponyms())
    for hypernym in hypernyms:
        count_hypernyms += len(hypernym.hyponyms())
    
    # Calculate the probability, assuming Poisson distribution
    # Number of synsets n = count_hyponyms + count_hypernyms
    # Lambda = (n / (count_hyponyms + count_hypernyms))
    n = count_hyponyms + count_hypernyms
    if n == 0:  # If no hyponyms or hypernyms, use log(1) = 0
        ic = 0
    else:
        # Calculating information content
        ic = -n / (count_hyponyms + count_hypernyms) * (n / (count_hyponyms + count_hypernyms))
        ic = (ic / 2 ) * (ic)/ (count_hyponyms + count_hypernyms)

    return ic

# Test the function
syn = wordnet.synsets('car')[0]  # Get a synset for 'car'
ic_value = calculate_ic(syn)
print(f'Information Content value for synset {syn.name()} is {ic_value}')
