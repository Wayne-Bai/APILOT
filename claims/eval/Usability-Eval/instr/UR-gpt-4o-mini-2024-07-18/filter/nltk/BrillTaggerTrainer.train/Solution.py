import nltk
from nltk.corpus import treebank
from nltk.tag import brill, brill_trainer
from nltk.tokenize import word_tokenize

# Load training data
train_sents = treebank.tagged_sents()

# Set parameters
max_rules = 100
min_score = 0
min_ac = 0.8

# Create a default tagger (for example, using the most common tag)
default_tagger = nltk.DefaultTagger('NN')

# Create a Brill trainer
trainer = brill_trainer.BrillTrainer(default_tagger, train_sents, 
                                      max_rules=max_rules, 
                                      min_score=min_score, 
                                      min_acc=min_ac)

# Train the Brill tagger
brill_tagger = trainer.train()
