import nltk
from nltk.corpus import wordnet

def get_synset_from_sense_key(sense_key):
    synset = wordnet.synset_from_pos_and_offset('verb', int(sense_key.split('.')[1]))
    return synset
