import nltk
from nltk.tag import brill, brill_trainer
from nltk.tbl import Template
from nltk.tag.brill_trainer import BrillTaggerTrainer
from nltk.corpus import treebank

# Load the treebank sentences
train_sents = treebank.tagged_sents()[:3000]

# Define a baseline tagger (e.g., a unigram tagger)
baseline_tagger = nltk.UnigramTagger(train_sents)

# Create Brill tagger templates
templates = [
    Template(brill.Pos([-1])),
    Template(brill.Pos([1])),
    Template(brill.Pos([-2])),
    Template(brill.Pos([2])),
    Template(brill.Pos([-2, -1])),
    Template(brill.Pos([1, 2])),
    Template(brill.Pos([-3, -2, -1])),
    Template(brill.Pos([1, 2, 3])),
    Template(brill.Pos([-1]), brill.Pos([1])),
    Template(brill.Word([-1])),
    Template(brill.Word([1])),
    Template(brill.Word([-2])),
    Template(brill.Word([2])),
    Template(brill.Word([-2, -1])),
    Template(brill.Word([1, 2])),
    Template(brill.Word([-3, -2, -1])),
    Template(brill.Word([1, 2, 3])),
    Template(brill.Word([-1]), brill.Word([1]))
]

# Initialize BrillTaggerTrainer
trainer = BrillTaggerTrainer(initial_tagger=baseline_tagger, templates=templates, trace=3)

# Train the Brill tagger with specific thresholds
max_rules = 200  # Define max number of rules
min_score = 2    # Minimum score for each rule
min_ac = 0.99    # Minimum accuracy for each rule

# Train the tagger
brill_tagger = trainer.train(train_sents, max_rules=max_rules, min_score=min_score, min_accuracy=min_ac)

# You can check the performance of the tagger or save it for later use
