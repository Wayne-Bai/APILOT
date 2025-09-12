from nltk.tag import BrillTagger
from nltk.corpus import brown
import random

# Load the training data
train_sents = brown.tagged_sents()

# Set the parameters
max_rules = 100
min_score = 0.5
min_ac = 0.9

# Initialize the Brill tagger
tagger = BrillTagger()

# Train the tagger
for i in range(max_rules):
    # Randomly select a set of sentences to train on
    train_set = random.sample(train_sents, 100)

    # Train the tagger on the selected sentences
    tagger.train(train_set)

    # Evaluate the tagger on a validation set
    val_sents = brown.tagged_sents(categories='news')
    val_score = tagger.score(val_sents)

    # If the improvement in score is less than min_score, break the loop
    if val_score > (i * 0.1) + min_score:
        break

# Print the final accuracy and number of rules
print("Final accuracy:", tagger.accuracy(train_sents))
print("Final number of rules:", tagger.num_rules)
