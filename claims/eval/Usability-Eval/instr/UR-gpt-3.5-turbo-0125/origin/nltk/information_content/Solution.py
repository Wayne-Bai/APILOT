
import math
from nltk.corpus import wordnet as wn

def calculate_ic(synset):
    hyponyms_count = len(wn.synset(synset).hyponyms())
    ic = -math.log(hyponyms_count / len(list(wn.all_synsets())))
    return ic
