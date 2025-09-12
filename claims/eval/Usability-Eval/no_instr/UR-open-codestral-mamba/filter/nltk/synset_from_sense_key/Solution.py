import nltk

# Ensure that the WordNet lexical database is downloaded
nltk.download('wordnet')

# Define the sense_key
sense_key = 'knock_knock.01'

# Retrieve synset based on the sense_key
synset = nltk.corpus.wordnet.synset(sense_key)

# Print the synset
print(synset)
