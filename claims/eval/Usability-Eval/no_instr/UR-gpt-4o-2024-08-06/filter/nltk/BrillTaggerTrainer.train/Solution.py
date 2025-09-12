import nltk
from nltk.tag import BrillTaggerTrainer, UnigramTagger
from nltk.corpus import treebank
from nltk.tag.brill import SymmetricProximateTokensTemplate, ProximateTokensTemplate, POS, Word

# Train the initial backoff tagger
train_sents = treebank.tagged_sents()[:3000]
test_sents = treebank.tagged_sents()[3000:]

# Defining a backoff tagger with UnigramTagger
backoff_tagger = UnigramTagger(train_sents)

# Create templates for the Brill Tagger
templates = [
    SymmetricProximateTokensTemplate(POS), 
    SymmetricProximateTokensTemplate(Word),
    ProximateTokensTemplate(-1, 0, [POS]), 
    ProximateTokensTemplate(-1, 0, [Word])
]

# Initialize and train the Brill Tagger
brill_trainer = BrillTaggerTrainer(initial_tagger=backoff_tagger, templates=templates, trace=3)
brill_tagger = brill_trainer.train(train_sents, max_rules=10, min_score=2, min_acc=0.99)

# Test the tagger and evaluate its performance
accuracy = brill_tagger.evaluate(test_sents)
print(f"Brill Tagger accuracy: {accuracy}")
