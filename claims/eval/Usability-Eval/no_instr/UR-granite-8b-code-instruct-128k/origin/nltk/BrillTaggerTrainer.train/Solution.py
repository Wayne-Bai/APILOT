import nltk
from nltk.tag import BrillTagger

# Define the corpus
train_sents = [("The", "DT"), ("quick", "JJ"), ("brown", "JJ"), ("fox", "NN"), ("jumped", "VBD"), ("over", "IN"), ("the", "DT"), ("lazy", "JJ"), ("dog", "NN")]

# Define the parameters
max_rules = 10
min_score = 0.2
min_ac = 0.7

# Train the Brill tagger
tagger = BrillTagger(train_sents, max_rules, min_score, min_ac)

# Print the trained tagger
print(tagger)
