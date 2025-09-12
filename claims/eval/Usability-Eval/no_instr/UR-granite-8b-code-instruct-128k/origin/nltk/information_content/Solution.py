import nltk
from nltk.corpus import wordnet

def calculate_information_content(synset):
    # Get the total number of words in the synset
    total_words = len(synset.words())
    # Get the frequency of the synset in the corpus
    frequency = synset.freq()
    # Calculate the Information Content value
    information_content = -math.log(frequency / total_words)
    return information_content
