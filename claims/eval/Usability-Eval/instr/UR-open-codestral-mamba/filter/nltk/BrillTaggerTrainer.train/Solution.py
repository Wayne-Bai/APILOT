import nltk
from nltk.tag import BrillTaggerTrainer
from nltk.tag import UnigramTagger, bigram_tagger

def train_brill_tagger(train_sents, max_rules, min_score, min_acc):
    unigram_tagger = UnigramTagger(train_sents)
    bigram_tagger = bigram_tagger(train_sents)

    template_list = [
        (nltk.tag.brill.SymmetricProximateTokensRule, (1, 1)),
        (nltk.tag.brill.SymmetricProximateTokensRule, (2, 2)),
        (nltk.tag.brill.SymmetricProximateTokensRule, (1, 2)),
        (nltk.tag.brill.SymmetricProximateTokensRule, (2, 1)),
        (nltk.tag.brill.ProximateTokensRule, (1, 1)),
        (nltk.tag.brill.ProximateTokensRule, (2, 2)),
        (nltk.tag.brill.ProximateTokensRule, (1, 2)),
        (nltk.tag.brill.ProximateTokensRule, (2, 1)),
        (nltk.tag.brill.ProximateTokensRule, (3,3)),
        (nltk.tag.brill.ProximateTokensRule, (2,3)),
        (nltk.tag.brill.ProximateTokensRule, (1,3)),
        (nltk.tag.brill.ProximateTokensRule, (3,2)),
        (nltk.tag.brill.ProximateTokensRule, (2,1)),
        (nltk.tag.brill.ProximateTokensRule, (3,1)),
        (nltk.tag.brill.ProximateTokensRule, (4,4)),
        (nltk.tag.brill.ProximateTokensRule, (3,4)),
        (nltk.tag.brill.ProximateTokensRule, (2,4)),
        (nltk.tag.brill.ProximateTokensRule, (1,4)),
        (nltk.tag.brill.ProximateTokensRule, (4,3)),
        (nltk.tag.brill.ProximateTokensRule, (3,2)),
        (nltk.tag.brill.ProximateTokensRule, (2,1)),
        (nltk.tag.brill.ProximateTokensRule, (4,2)),
        (nltk.tag.brill.ProximateTokensRule, (3,1)),
        (nltk.tag.brill.ProximateTokensRule, (4,1)),
        ]

    brill_trainer = BrillTaggerTrainer(initial_tagger=bigram_tagger,
                                   templates=template_list,
                                   trace=3,
                                   deterministic=True)

    brill_tagger = brill_trainer.train(train_sents, max_rules=max_rules,
                                       min_score=min_score, min_acc=min_acc)

    return brill_tagger

# Assuming train_sents is already defined
train_sents = nltk.corpus.brown.tagged_sents(categories='news')
max_rules = 30
min_score = 3
min_acc = 0.95

brill_tagger = train_brill_tagger(train_sents, max_rules, min_score, min_acc)
print('Brill Tagger Training Complete')
