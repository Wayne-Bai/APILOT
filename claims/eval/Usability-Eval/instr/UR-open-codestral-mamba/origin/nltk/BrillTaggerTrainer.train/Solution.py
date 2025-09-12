import nltk
from nltk.tag import BrillTaggerTrainer

# Define the maximum number of rules and minimum score and accuracy
max_rules = 30
min_score = 5
min_ac = 0.95

# Fetch the corpus train_sents for training
nltk.download('treebank')
train_sents = nltk.corpus.treebank.tagged_sents()

# Prepare the tagger
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)

# Train the Brill tagger
templates = nltk.brill_trainer.brill_trainer.Template._rules
trainer = BrillTaggerTrainer(initial_tagger=t2, templates=templates, trace=3)
brill_tagger = trainer.train(train_sents, max_rules=max_rules, min_score=min_score, min_acc=min_ac)

# Test the model
test_sents = nltk.corpus.treebank.tagged_sents(fileids=['23'])
print(brill_tagger.evaluate(test_sents))
