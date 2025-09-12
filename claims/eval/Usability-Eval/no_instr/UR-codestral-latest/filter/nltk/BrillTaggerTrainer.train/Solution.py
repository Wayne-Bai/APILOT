import nltk
from nltk.tag import brill
from nltk.tbl import Template

# Training data
train_sents = [...]

# Initialize brill tagger with default templates
tagger = brill.BrillTaggerTrainer(nltk.DefaultTagger('NN'), Template())

# Train the tagger
tagger.train(train_sents, max_rules=10, min_score=2, min_acc=0.90)

# Print the rules
print(tagger.rules())
