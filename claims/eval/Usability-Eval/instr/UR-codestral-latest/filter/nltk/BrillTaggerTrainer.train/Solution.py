import nltk
from nltk.tag import brill, brill_trainer

def train_brill_tagger(train_sents, max_rules, min_score, min_ac):
    templates = brill_trainer.brill_template_generator()
    trainer = brill_trainer.BrillTaggerTrainer(initial_tagger=nltk.DefaultTagger('NN'),
                                              templates=templates,
                                              trace=3,
                                              max_rules=max_rules,
                                              min_score=min_score,
                                              min_acc=min_ac)
    tagger = trainer.train(train_sents)
    return tagger

# Example usage:
# Replace train_sents, and the values for max_rules, min_score, and min_ac with your actual values.
# train_sents = [(('John', 'Thinks'), 'NN'), (('Mary', 'Read'), 'NN')]
# max_rules = 10
# min_score = 5
# min_ac = 0.9

# tagger = train_brill_tagger(train_sents, max_rules, min_score, min_ac)
