
import nltk
from nltk.corpus import wordnet as wn

def retrieve_synset_from_sense_key(sense_key):
    offset = int(sense_key.split(':')[0])
    part_of_speech = sense_key.split(':')[3]
    
    if part_of_speech == 'n':
        pos = wn.NOUN
    elif part_of_speech == 'v':
        pos = wn.VERB
    elif part_of_speech == 'a':
        pos = wn.ADJ
    elif part_of_speech == 'r':
        pos = wn.ADV
    else:
        pos = None

    if pos:
        synsets = wn.synsets(offset=offset, pos=pos)
        return synsets
    else:
        return None
