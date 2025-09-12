from nltk.corpus import wordnet

def calculate_information_content(synset):
    ic = wordnet.ic(synset)
    return ic
