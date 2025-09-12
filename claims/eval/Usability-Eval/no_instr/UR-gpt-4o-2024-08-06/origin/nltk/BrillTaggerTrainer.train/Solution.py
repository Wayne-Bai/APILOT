import nltk
from nltk.tag import brill
from nltk.tag import untag
from nltk.corpus import treebank

# Assuming train_sents is a list of tagged sentences for training
train_sents = treebank.tagged_sents()

# Specify the max_rules, min_score, and min_ac
max_rules = 200
min_score = 2
min_ac = 0.9

# Define the initial tagger, e.g., an UnigramTagger
baseline_tagger = nltk.UnigramTagger(train_sents)

# Define templates for the Brill Tagger transformation rules
templates = brill.fntbl37()

# Initialize the Brill Tagger Trainer
trainer = brill.BrillTaggerTrainer(
    initial_tagger=baseline_tagger, 
    templates=templates, 
    trace=3
)

# Train the Brill Tagger
brill_tagger = trainer.train(
    train_sents, 
    max_rules=max_rules,
    min_score=min_score
)

# Example usage for evaluation purposes
test_sents = treebank.tagged_sents()[3000:]  # Use a subset of sentences for testing
accuracy = brill_tagger.evaluate(test_sents)
print("Brill Tagger Accuracy:", accuracy)
