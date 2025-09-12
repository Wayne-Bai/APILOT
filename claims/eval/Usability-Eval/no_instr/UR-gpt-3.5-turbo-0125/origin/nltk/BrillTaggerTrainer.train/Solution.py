
import nltk
from nltk.tag import brill
from nltk.tbl import demo as brill_demo

# Define the parameters
train_sents = brill_demo.NE_BIO_TAGGED_SENTENCES
max_rules = 200
min_score = 2
min_ac = 0

# Train the Brill tagger
template = brill.Pos, brill.Word
brill_tagger = brill_trainer.train(train_sents, max_rules, min_score, min_ac, template)

print(brill_tagger.rules())
