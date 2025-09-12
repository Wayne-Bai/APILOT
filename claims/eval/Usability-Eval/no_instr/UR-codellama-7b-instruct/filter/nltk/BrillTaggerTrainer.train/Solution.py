
import nltk
from nltk.tag import BrillTagger
from nltk.corpus import treebank

train_sents = treebank.tagged_sents()
max_rules = 10
min_score = -2
min_ac = 0.9

# Create a Brill tagger using the corpus
brill_tagger = BrillTagger(train_sents, max_rules=max_rules, min_score=min_score)

# Train the tagger on the corpus
brill_tagger.train()

# Print the tagger's rules
print(brill_tagger.rules)
