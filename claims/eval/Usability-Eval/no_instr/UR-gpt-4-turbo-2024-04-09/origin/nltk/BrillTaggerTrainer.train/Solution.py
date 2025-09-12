import nltk
from nltk.tag import brill, brill_trainer
from nltk.tbl import Template
from nltk.tag.brill import Pos, Word
from nltk.corpus import treebank

# Load the training sentences from treebank or another corpus
train_sents = treebank.tagged_sents()[:3000]

# First, create a baseline tagger (e.g. UnigramTagger)
unigram_tagger = nltk.UnigramTagger(train_sents)

# Define a set of templates for the Brill tagger transformations
templates = [
    Template(Pos([-1])), Template(Pos([1])),
    Template(Pos([-2])), Template(Pos([2])),
    Template(Pos([-1, 1])), Template(Pos([-2, -1])),
    Template(Pos([1, 2])), Template(Pos([-2, -1, 1])),
    Template(Pos([-1, 1, 2])), Template(Pos([-3, -2, -1])),
    Template(Word([-1])), Template(Word([1])),
    Template(Word([-2])), Template(Word([2])),
    Template(Word([-1, 1])), Template(Word([-2, -1])),
    Template(Word([1, 2])), Template(Word([-2, -1, 1])),
    Template(Word([-1, 1, 2])), Template(Word([-3, -2, -1])),
]

# Parameters for training
max_rules = 200  # maximum number of rules
min_score = 2    # minimum score for a rule to be considered
min_ac = 0.9     # minimum accuracy

# Train the Brill tagger
trainer = brill_trainer.BrillTaggerTrainer(initial_tagger=unigram_tagger,
                                           templates=templates,
                                           trace=3)
brill_tagger = trainer.train(train_sents, max_rules=max_rules, min_score=min_score)

# Optionally, check the tagger's performance
# print(brill_tagger.evaluate(some_test_sents))

# To use the trained Brill tagger:
# tagged = brill_tagger.tag(nltk.word_tokenize("Your test sentence here."))
# print(tagged)
