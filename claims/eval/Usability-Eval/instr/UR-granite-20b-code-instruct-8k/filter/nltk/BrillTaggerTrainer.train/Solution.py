import nltk
from nltk.tag import BrillTagger
from nltk.corpus import brown

train_sents = brown.tagged_sents(categories=['adventure', 'fiction', 'romance'])

brill_tagger = BrillTagger(train_sents)

