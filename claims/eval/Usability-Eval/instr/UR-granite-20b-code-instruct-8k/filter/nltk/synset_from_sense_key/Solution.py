import nltk

# Define the sense_key
sense_key = 'air.air_quality.health'

# Retrieve the synset based on the sense_key
synset = nltk.corpus.wordnet.synset(sense_key)

# Print the synset
print(synset)
