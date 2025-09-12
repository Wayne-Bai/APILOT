import nltk
from nltk.tag import BrillTagger, brill_fnt, brill_tb
from nltk.corpus import treebank

# Ensure the treebank corpus is downloaded
nltk.download('treebank')

# Load the treebank corpus for training and testing
train_sents = treebank.tagged_sents()[:3000]
test_sents = treebank.tagged_sents()[3000:]

# Define the Brill tagger trainer with the desired parameters
bt = BrillTagger(
    train_sents,
    brill_fnt(),  # Template for forward and nominal suffix transformations
    brill_tb(),  # Template for brill tagger base rules
    max_rules=200,  # Maximum number of transformations
    min_score=2,  # Minimum net error reduction
    min_acc=0.97  # Minimum accuracy required for each transformation
)

# Print the accuracy of the Brill tagger
print("Accuracy:", bt.evaluate(test_sents))
