import nltk
from nltk.tag import BrillTaggerTrainer

def train_brill_tagger(train_sents, max_rules, min_score, min_acc):
    # Define a function to train the Brill tagger
    def brill_trainer(trainer):
        return nltk.tag.BrillTaggerTrainer(initial_tagger=nltk.tag.UnigramTagger(train_sents),
                                           trace=3,
                                           determine=trainer,
                                           rules_factory=nltk.tag.brill.fast_rule_generator(min_acc=min_acc))

    # Train the Brill tagger
    tagger = BRILLExtended(train_sents)
    brill_trainer = brill_trainer(BrillTrainer)
    tagger.train(train_sents, max_rules, min_score, brill_trainer)

    return tagger

# example usage
train_sents = nltk.corpus.brown.tagged_sents()
max_rules = 20
min_score = 5
min_acc = 0.7
tagger = train_brill_tagger(train_sents, max_rules, min_score, min_acc)
print(tagger)
