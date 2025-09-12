import nltk
from nltk import BrillTaggerTrainer

# Assuming you have a list of tagged sentences: train_sents
# train_sents = [(('John', 'DT'), ('loves', 'VBZ'), ('Mary', 'NN')), ...]

# Define the number of rules for the Brill tagger to produce
max_rules = 100

# Define the minimum score for each transformation
min_score = 3

# Define the minimum accuracy for each transformation
min_ac = 0.7

# Initialize a default UnigramTagger
default_tagger = nltk.UnigramTagger(train_sents)

# Initialize a BrillTaggerTrainer with the default tagger
trainer = BrillTaggerTrainer(default_tagger, train_sents, trace=3)

# Train the Brill tagger with the defined parameters
brill_tagger = trainer.train(max_rules=max_rules, min_score=min_score, min_acc=min_ac)

print("Accuracy of the Brill tagger:", brill_tagger.evaluate(test_sents))
