import nltk
from nltk.tag import brill, brill_trainer

# Define a function for training a Brill tagger
def train_brill_tagger(train_sents, max_rules, min_score, min_ac):
    # Create the tagger from the corpus
    tagger = brill_trainer.BrillTaggerTrainer(initial_tagger = nltk.tag.UnigramTagger(train_sents),
                                              features = nltk.tag.brill.nltk_tagger_features2,
                                              trace = 0)

    # Iteratively apply rules until convergence or until there are max_rules
    iter = 0
    while iter < max_rules:
        rules = tagger.train(train_sents, max_rules = max_rules, min_score = min_score, min_acc = min_ac)
        iter += 1
    return tagger.tagger()

# Assuming train_sents is a list of tagged sentences, max_rules, min_score, min_ac are given as above,
# then use the trained tagger as below
tagger = train_brill_tagger(train_sents, max_rules, min_score, min_ac)
tagger.tag(test_sentence)
