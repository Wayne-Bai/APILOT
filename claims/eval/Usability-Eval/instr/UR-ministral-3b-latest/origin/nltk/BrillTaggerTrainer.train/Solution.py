import nltk

# Ensure you have the necessary datasets
nltk.download('popular')
nltk.download('tagged')

# Load the corpus
train_sents = nltk.corpus.treebank_sents()

# Load Brill Tagger
from nltk.tag import BrillTagger
brill_tagger = BrillTagger()

# Train the Brill Tagger
brill_tagger.train(train_sents, max_rules=10, min_score=0.5, min_ac=0.8)

# Use the trained Brill Tagger
test_sent = ["The cat sat on the mat."]
tagged_sent = brill_tagger.tag(test_sent)

for word, tag in tagged_sent:
    print(f"{word} -> {tag}")
