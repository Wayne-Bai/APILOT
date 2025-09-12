import nltk
from nltk.corpus import wordnet as wn
from nltk.semantics import WordNetLemmatizer

def get_synset(sense_key):
    """Retrieves synset based on a given sense_key"""
    # Get the word and pos from the sense_key
    word, pos = sense_key.split('-')
    
    # Look up the synset for the word using WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    lemma = lemmatizer.lemmatize(word)
    synsets = wn.synsets(lemma, pos=pos)
    
    # Find the correct synset based on the sense_key
    for synset in synsets:
        if sense_key == '-'.join([synset.name(), str(synset.offset())]):
            return synset
    
    # If no matching synset is found, raise a ValueError
    raise ValueError('No synset found for sense_key {}'.format(sense_key))
