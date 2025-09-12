
import nltk
from nltk.tag import brill

train_sents = ...  # List of training sentences
max_rules = 10
min_score = 2
min_ac = 0.9

templates = brill.fntbl37()
trainer = brill_trainer.BrillTaggerTrainer(brill_templates=templates, trace=3, deterministic=True)
tagger = trainer.train(train_sents, max_rules=max_rules, min_score=min_score, min_ac=min_ac)
