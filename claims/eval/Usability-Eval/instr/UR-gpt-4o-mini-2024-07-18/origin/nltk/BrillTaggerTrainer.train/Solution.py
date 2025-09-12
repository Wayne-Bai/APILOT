import nltk
from nltk.tag import StaticBackoffTagger
from nltk.tag import brill, brill_trainer
from nltk.corpus import treebank

# Prepare training data
train_sents = treebank.tagged_sents()[:300]  # Use first 300 sentences for training

# Define your parameters
max_rules = 200  # Maximum number of transformation rules
min_score = 0.5  # Minimum score reduction in errors
min_ac = 0.8     # Minimum accuracy required

# Create a backoff tagger - here you could use your initial tagger
initial_tagger = StaticBackoffTagger(nltk.DefaultTagger('NN'))

# Train the Brill tagger
trainer = brill_trainer.BrillTaggerTrainer(initial_tagger, 
                                            train_sents, 
                                            max_rules=max_rules, 
                                            min_score=min_score, 
                                            min_accuracy=min_ac)

brill_tagger = trainer.train(train_sents)

# Example of how to use the trained tagger
test_sentence = "The quick brown fox jumps over the lazy dog".split()
tagged_sentence = brill_tagger.tag(test_sentence)

print(tagged_sentence)
