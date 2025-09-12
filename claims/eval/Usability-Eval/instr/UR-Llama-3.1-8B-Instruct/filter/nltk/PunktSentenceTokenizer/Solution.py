# Import required libraries
import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
import re

# Download necessary NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
