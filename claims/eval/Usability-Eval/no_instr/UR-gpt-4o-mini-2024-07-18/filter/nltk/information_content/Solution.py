import nltk
from nltk.corpus import wordnet as wn

def calculate_information_content(synset):
    # Get the frequency distribution of synsets in the WordNet corpus
    freq_dist = wn.synset(synset).wup_similarity(wn.synset('entity.n.01'))  # Example to get a base similarity, adjust as needed
    information_content = -1 * freq_dist.log() if freq_dist > 0 else float('inf')  # Avoid log(0)
    return information_content

# Example usage
synset_name = 'dog.n.01'  # Replace with your desired synset
info_content = calculate_information_content(synset_name)
print(f'Information content for {synset_name}: {info_content}')
