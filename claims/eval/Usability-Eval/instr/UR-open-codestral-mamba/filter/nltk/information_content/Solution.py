import nltk
from nltk.corpus import wordnet as wn

def information_content(synset):
    # Total number of word senses in the WordNet corpus
    total_count = sum([len(ss.lemmas()) for ss in wn.all_synsets()])

    # Number of word senses in this synset
    synset_count = len(synset.lemmas())

    return -log(synset_count / total_count)

# Example usage:
synset = wn.synset('dog.n.01') # Example synset for the word "dog"
ic = information_content(synset)
print(f"Information Content for {synset.lemmas()[0].name()}: {ic}")
