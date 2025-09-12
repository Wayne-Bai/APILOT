import nltk
from nltk.corpus import treebank
from nltk.tag import brill, brill_trainer

# Define training and testing data
train_sents = treebank.tagged_sents()[:3000]  # Using a subset of the treebank corpus
test_sents = treebank.tagged_sents()[3000:]  # Remaining sentences for testing

# Define initial tagger (basic regex tagger or any other tagger of your choice)
initial_tagger = nltk.UnigramTagger(train_sents)

# Define the Brill Trainer with the specified parameters
max_rules = 200  # maximum number of transformations
min_score = 0    # minimum score to reduce error
min_ac = 0.6     # minimum accuracy

# Create a Brill trainer
brill_tagger = brill.Trainer(initial_tagger, train_sents, max_rules=max_rules, min_score=min_score, min_ac=min_ac)

# Train the Brill tagger
trained_tagger = brill_tagger.train()

# Evaluate the trained tagger on test data
accuracy = trained_tagger.evaluate(test_sents)
print(f'Trained Brill Tagger Accuracy: {accuracy:.2f}')
