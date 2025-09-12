from nltk.corpus import wordnet

def calculate_information_content(synset):
    synset_id = synset.id()
    synset_hash = hash(synset_id)

    synset_frequency = synset.frequency()
    synset_pairs = synset.lemmas()

    information_content = synset_frequency / (len(synset_pairs) * 1.0)

    return information_content

# Example usage:
synset = wordnet.synset('car.n.01')
print(calculate_information_content(synset))
