import nltk
from nltk.data import corpus

# Download necessary data files if not already present
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('omw-1.43')

# Import wordnet module
from nltk.corpus import wordnet as wn

def get_information_content(synset):
    corpus_count = len(corpus)
    popular_count = len(wn.synsets(synset))

    # Calculate the information content value
    information_content = corpus_count / popular_count
    print(f'The Information Content value for synset "{synset}" is {information_content}')

# You can use the following synset as an example:
synset = 'apple.n.01'
get_information_content(synset)
