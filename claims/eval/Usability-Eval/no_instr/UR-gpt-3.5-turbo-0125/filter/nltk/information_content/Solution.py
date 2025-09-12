
# Importing necessary modules from nltk
from nltk.corpus import wordnet as wn

# Function to calculate the Information Content value for a synset
def calculate_information_content(synset):
    all_synsets = list(wn.all_synsets())
    freq_count = 0
    for s in all_synsets:
        freq_count += s.count()
    
    information_content = -1 * (synset.count() / freq_count)
    return information_content

# Example usage
word_synset = wn.synsets('dog')[0]  # Get the synset for the word 'dog'
ic_value = calculate_information_content(word_synset)
print("Information Content Value for", word_synset.name(), "is:", ic_value)
