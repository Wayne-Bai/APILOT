import nltk
from nltk.tag import brill

# Assume train_sents is your prepared training data and defined here
# train_sents = [.....]

# Define templates
templates = brill.fntbl37()

# Create a new Brill tagger
brill_tagger = brill.BrillTaggerTrainer(initial_tagger=nltk.DefaultTagger('NN'), templates=templates)

# Train the Brill tagger
brill_tagger = brill_tagger.train(train_sents, max_rules=10, min_score=2, min_acc=0.8)

# Now you can use the trained tagger to tag your data
# tags = brill_tagger.tag([....])
