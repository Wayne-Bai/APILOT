import nltk
from nltk.tag import brill, brill_trainer
from nltk.tag import UnigramTagger, BrillTaggerTrainer

# Assuming train_sents is a list of sentences where each sentence is a list of (word, tag) tuples
# Example: train_sents = [[(word1, tag1), (word2, tag2)], [(word3, tag3), (word4, tag4)]]

# Define the initial tagger (UnigramTagger)
initial_tagger = UnigramTagger(train_sents)

# Define the Brill template
templates = [
    brill.Template(brill.Pos([-1])),
    brill.Template(brill.Pos([1])),
    brill.Template(brill.Word([-1])),
    brill.Template(brill.Word([1])),
    brill.Template(brill.Pos([-1]), brill.Pos([1])),
]

# Train the Brill tagger
brill_tagger = BrillTaggerTrainer(initial_tagger, templates).train(train_sents, max_rules=max_rules, min_score=min_score, min_acc=min_ac)

# Now brill_tagger is trained and can be used for tagging new sentences
