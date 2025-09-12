import nltk
from nltk.corpus import wordnet

# Choose a synset
synset = wordnet.synset('dog.n.01')

# Calculate the Information Content value
ic_value = nltk.corpus.wordnet_ic.ic(synset, False)

# Print the result
print("The Information Content value for the synset", synset, "is", ic_value)
