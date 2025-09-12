
import nltk
from nltk.corpus import wordnet

def calculate_information_content(synset):
    # Get the number of words in the synset
    num_words = len(synset.words())
    
    # Get the total number of synsets in the WordNet corpus
    total_synsets = len(wordnet.all_synsets())
    
    # Calculate the information content
    information_content = -math.log2(num_words / total_synsets)
    
    return information_content
