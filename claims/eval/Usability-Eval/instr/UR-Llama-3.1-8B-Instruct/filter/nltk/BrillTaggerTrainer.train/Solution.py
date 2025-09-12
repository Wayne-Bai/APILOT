# Import required libraries
import nltk
from nltk import RegexpTagger, UnigramTagger, BigramTagger
from nltk import overwrite_vocabulary
from nltk.tag import BrillTaggerTrainer
from nltk.corpus import treebank
nltk.download('treebank')
