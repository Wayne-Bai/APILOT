import nltk
from nltk.tag import BrillTagger
from nltk.corpus import Brown

# Load the training data
train_sents = Brown.tagged_sents()

# Set the parameters for the Brill tagger
max_rules = 100
min_score = 0.5
min_ac = 0.9

# Initialize the Brill tagger
tagger = BrillTagger()

# Train the tagger
tagger.train(train_sents, max_rules=max_rules, min_score=min_score, min_ac=min_ac)
