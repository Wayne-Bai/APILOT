import nltk
from nltk.util import *
from nltk.tokenize import sent_tokenize
from nltk.corpus import markov

# Make sure to download required data
import nltk
nltk.download('punkt')

def sentence_tokenizer():
    # Load English corpus
    English = markov.CorpusReader('path/to/text')

    # Create model for abbreviation words, collocations, and sentence start words
    model = markov.Model()
    for i in ' '.join(English.raw()):
        model.write('i')

    # Tokenize using the model
    sentences = sent_tokenize('Your sentence goes here')

    return sentences

# Estimate performance
corpus_path = 'path/to/text'  # adjust this to your actual text corpus
sent_tokenizer(corpus_path)
