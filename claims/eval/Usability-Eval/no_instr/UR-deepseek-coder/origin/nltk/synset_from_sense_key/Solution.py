import nltk
from nltk.corpus import wordnet

def get_synset_from_sense_key(sense_key):
    # Split the sense_key to extract lemma and synset_key
    lemma, synset_key = sense_key.split('%')
    
    # Extract the part of speech (pos) from the synset_key
    pos = synset_key[0]
    
    # Extract the lexname_index and lex_id from the synset_key
    lexname_index, lex_id = map(int, synset_key[1:].split(':'))
    
    # Retrieve the synset using the lemma and pos
    synsets = wordnet.synsets(lemma, pos=pos)
    
    # Filter synsets to find the one matching the lexname_index and lex_id
    for synset in synsets:
        if synset._lexname_index == lexname_index and synset._lex_id == lex_id:
            return synset
    
    return None

# Example usage
sense_key = "dog%1:05:00::"
synset = get_synset_from_sense_key(sense_key)
if synset:
    print(f"Synset: {synset}")
else:
    print("Synset not found.")
