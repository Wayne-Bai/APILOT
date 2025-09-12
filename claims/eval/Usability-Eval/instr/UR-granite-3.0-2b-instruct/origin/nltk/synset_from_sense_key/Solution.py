from nltk.corpus import wordnet

def get_synset_by_sense_key(sense_key):
    synsets = wordnet.synsets(sense_key)
    if synsets:
        return synsets[0]
    else:
        return None
