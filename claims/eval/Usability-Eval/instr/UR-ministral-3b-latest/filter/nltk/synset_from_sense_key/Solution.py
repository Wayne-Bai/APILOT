from nltk.corpus import wordnet

# Example: Retrieves synset based on a given sense_key
word = "play"
synset = wordnet.synsets(word, pos=wordnet.NOUN)

for s in synset:
    print(s.name())
