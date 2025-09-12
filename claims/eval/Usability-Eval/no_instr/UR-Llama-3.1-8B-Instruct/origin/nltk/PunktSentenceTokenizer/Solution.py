# Importing necessary libraries
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import brown
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.tokenize import RegexpTokenizer
