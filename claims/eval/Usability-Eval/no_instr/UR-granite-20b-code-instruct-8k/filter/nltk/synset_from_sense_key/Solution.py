import nltk
def get_synset(sense_key):
    synset = nltk.corpus.wordnet.synset(sense_key)
    return synset
