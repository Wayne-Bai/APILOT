import nltk
from nltk.tag import brill, brill_trainer
from nltk.tag import UnigramTagger
from nltk.corpus import treebank

# Assuming train_sents is a part of the treebank corpus
train_sents = treebank.tagged_sents()[:3000]

# Initial tagger for Brill training
unigram_tagger = UnigramTagger(train_sents)

# Training Brill Tagger
templates = [
    brill.Template(brill.Pos([1, 1])),
    brill.Template(brill.Pos([1])),
]

# Initializing Brill Trainer
trainer = brill_trainer.BrillTaggerTrainer(
    initial_tagger=unigram_tagger, 
    templates=templates, 
    trace=3
)

# Set training parameters
max_rules = 10
min_score = 2
min_ac = 0.95

# Train the tagger
brill_tagger = trainer.train(train_sents, max_rules=max_rules, min_score=min_score, min_acc=min_ac)

# Optionally, test the trained tagger
test_sents = treebank.tagged_sents()[3000:]
print(brill_tagger.evaluate(test_sents))
