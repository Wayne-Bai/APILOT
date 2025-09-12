import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
nltk.download('wordnet')
nltk.download('wordnet_ic')

# Load an information content file
ic = wordnet_ic.ic('ic-brown.dat')

# Get synsets for a particular word
synsets = wn.synsets('dog')

# Choose a synset to work with
dog_synset = synsets[0]

# Calculate the information content of the synset
info_content = ic.information_content(dog_synset)

print(f'Information Content of the synset {dog_synset}: {info_content}')
