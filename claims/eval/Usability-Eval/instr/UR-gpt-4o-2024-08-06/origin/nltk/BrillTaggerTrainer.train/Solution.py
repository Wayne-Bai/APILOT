import nltk
from nltk.corpus import treebank
from nltk.tag import UnigramTagger, BigramTagger
from nltk.tag.brill import BrillTaggerTrainer, Template
from nltk.tag.brill_trainer import Pos, Word
from nltk.corpus.reader import TaggedCorpusReader

# Sample training data
train_sents = treebank.tagged_sents()[:3000]

# Define template
templates = [
    Template(Pos([-1])), Template(Pos([1])),
    Template(Pos([-2])), Template(Pos([2])),
    Template(Pos([-2, -1])), Template(Pos([1, 2])),
    Template(Word([-1])), Template(Word([1])),
    Template(Word([-2])), Template(Word([2])),
    Template(Word([-2, -1])), Template(Word([1, 2]))
]

# Define initial tagger
initial_tagger = BigramTagger(train_sents, backoff=UnigramTagger(train_sents))

# Parameters for BrillTaggerTrainer
max_rules = 200
min_score = 3
min_acc = 0.95

# Train the Brill Tagger
trainer = BrillTaggerTrainer(initial_tagger, templates, trace=3)
brill_tagger = trainer.train(train_sents, max_rules=max_rules, min_score=min_score)

# Validate accuracy
accuracy = brill_tagger.evaluate(train_sents)
if accuracy >= min_acc:
    print(f"Brill tagger trained with accuracy: {accuracy:.4f}")
else:
    print("Trained Brill tagger did not meet minimum accuracy requirement.")
