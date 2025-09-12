import nltk
from nltk.corpus import wordnet as wn
from collections import defaultdict
import math

# Ensure you have the required resources
nltk.download('wordnet')
nltk.download('wordnet_ic')

def compute_ic(synset, freq_dist, total_count):
    """
    Compute the information content of a given synset.
    
    :param synset: WordNet synset for which IC is to be computed
    :param freq_dist: Frequency distribution of word occurrences
    :param total_count: Total count of words in the corpus
    :return: Information content of the synset
    """
    synset_name = synset.name()
    # Calculate the probability of the synset
    prob = freq_dist[synset_name] / total_count

    # The log probability gives the information content,
    # ensuring no division-by-zero errors
    if prob > 0:
        return -math.log(prob)
    else:
        return 0

def generate_freq_dist(corpus):
    """
    Generate the frequency distribution of synsets in a given corpus.
    
    :param corpus: The corpus to analyze
    :return: A dictionary with synset frequency and total word count
    """
    freq_dist = defaultdict(int)
    total_count = 0

    # Counting occurrences of each synset
    for sentence in corpus:
        for word in sentence:
            synsets = wn.synsets(word)
            if synsets:
                synset_name = synsets[0].name()
                freq_dist[synset_name] += 1
                total_count += 1
    
    return freq_dist, total_count

# Example corpus: list of lists of words
corpus = [
    ['dog', 'barks'],
    ['cat', 'meows'],
    ['bird', 'flies'],
    # Add more contexts and words as needed
]

# Generate frequency distribution for the corpus
freq_dist, total_count = generate_freq_dist(corpus)

# Calculate the information content for a given synset, e.g., 'dog.n.01'
synset_example = wn.synset('dog.n.01')
ic_value = compute_ic(synset_example, freq_dist, total_count)

print(f"Information Content of '{synset_example.name()}': {ic_value}")
