import nltk
from nltk.tag import brill
from nltk.tbl.template import Template
from nltk.tag.brill import Pos, Word
from nltk.corpus import treebank
from nltk.tag import UnigramTagger, BrillTaggerTrainer

# Load the training sentences from the treebank corpus
train_sents = treebank.tagged_sents()[:3000]

# Set up the initial tagger (e.g., a Unigram Tagger)
initial_tagger = UnigramTagger(train_sents)

# Define Brill Tagger templates
templates = [
    Template(Pos([-1])), Template(Pos([1])),
    Template(Pos([-2])), Template(Pos([2])),
    Template(Pos([-1, -2])), Template(Pos([1, 2])),
    Template(Pos([-2, -1])), Template(Pos([2, 1])),
    Template(Pos([-3, -2, -1])), Template(Pos([1, 2, 3])),
    Template(Pos([-1]), Pos([1])), Template(Word([-1])),
    Template(Word([1])), Template(Word([-2, -1])),
    Template(Word([1, 2]))
]

# Create the Brill tagger trainer
trainer = BrillTaggerTrainer(initial_tagger, templates, deterministic=True)

# Train the Brill tagger with specific parameters
max_rules = 200  # maximum number of rules
min_score = 2    # minimum score of each rule
min_ac = 0.5     # minimum accuracy of each rule

# Here, the 'train' method does not explicitly filter by 'min_ac' due to limitations in the NLTK implementation
brill_tagger = trainer.train(train_sents, max_rules=max_rules, min_score=min_score)

# Optionally, print or inspect the learned rules
for rule in brill_tagger.rules():
    print(rule)
