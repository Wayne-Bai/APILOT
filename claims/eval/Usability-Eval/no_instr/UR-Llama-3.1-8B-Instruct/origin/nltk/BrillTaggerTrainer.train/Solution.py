import nltk
from nltk.tag import BrillTaggerTrainer
from nltk.corpus import treebank

# Ensure the desired NLTK data is available and download them if necessary
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('treebank')
