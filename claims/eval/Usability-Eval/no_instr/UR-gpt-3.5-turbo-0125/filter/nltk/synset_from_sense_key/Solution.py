
import nltk
from nltk.corpus import wordnet as wn

# Given sense key
sense_key = "bank%1:17:00::"

# Retrieve synset based on the given sense key
synset = wn.lemma_from_key(sense_key).synset()

print(synset)
