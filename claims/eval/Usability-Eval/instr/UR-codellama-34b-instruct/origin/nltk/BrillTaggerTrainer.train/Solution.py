
import nltk
from nltk.tag import BrillTagger
from nltk.corpus import brown

# Load the Brown Corpus
brown_sents = brown.sents()

# Train the Brill Tagger on the corpus
brill_tagger = BrillTagger(train=brown_sents, max_rules=1000, min_score=10, min_ac=85)

# Evaluate the tagger on a new sentence
test_sentence = 'The quick brown fox jumps over the lazy dog .'.split()
tagged_sentence = brill_tagger.tag(test_sentence)
print(tagged_sentence)
