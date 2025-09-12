import nltk
from nltk.tag import brill, brill_trainer
from nltk.tag import UnigramTagger

def train_brill_tagger(train_sents, max_rules, min_score, min_acc):
    # Initialize a baseline tagger (UnigramTagger)
    baseline_tagger = UnigramTagger(train_sents)
    
    # Define the feature detector function
    templates = [
        brill.Template(brill.Pos([-1])),
        brill.Template(brill.Pos([1])),
        brill.Template(brill.Pos([-2])),
        brill.Template(brill.Pos([2])),
        brill.Template(brill.Pos([-2, -1])),
        brill.Template(brill.Pos([1, 2])),
        brill.Template(brill.Pos([-3, -2, -1])),
        brill.Template(brill.Pos([1, 2, 3])),
        brill.Template(brill.Word([-1])),
        brill.Template(brill.Word([1])),
        brill.Template(brill.Word([-2])),
        brill.Template(brill.Word([2])),
        brill.Template(brill.Word([-2, -1])),
        brill.Template(brill.Word([1, 2])),
        brill.Template(brill.Word([-3, -2, -1])),
        brill.Template(brill.Word([1, 2, 3]))
    ]
    
    # Train the Brill tagger
    brill_tagger = brill_trainer.BrillTaggerTrainer(baseline_tagger, templates, trace=3)
    trained_tagger = brill_tagger.train(train_sents, max_rules=max_rules, min_score=min_score, min_acc=min_acc)
    
    return trained_tagger

# Example usage
# train_sents = [ ... ]  # Your training sentences in the format [(word, tag), ...]
# max_rules = 100
# min_score = 2
# min_acc = 0.95
# trained_tagger = train_brill_tagger(train_sents, max_rules, min_score, min_acc)
