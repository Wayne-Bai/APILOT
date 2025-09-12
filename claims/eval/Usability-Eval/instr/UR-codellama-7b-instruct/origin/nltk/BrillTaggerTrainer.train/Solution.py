
import nltk
from nltk.corpus import train_sents
from nltk.tag import brill_trainer

# Set up the Brill trainer
trainer = brill_trainer(train_sents, max_rules=100, min_score=0.5, min_ac=0.7)

# Train the tagger
tagger = trainer.train()

# Print the tagger
print(tagger)
