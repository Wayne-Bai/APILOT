import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
nltk.download('wordnet')
nltk.download('wordnet_ic')

# Load an information content file
ic = wordnet_ic.ic('ic-brown.dat')

# Define the synset for which you want to calculate the Information Content
synset = wn.synset('dog.n.01')

# Calculate the Information Content of the synset
info_content = synset.information_content(ic)
print("Information Content of the synset 'dog.n.01':", info_content)
