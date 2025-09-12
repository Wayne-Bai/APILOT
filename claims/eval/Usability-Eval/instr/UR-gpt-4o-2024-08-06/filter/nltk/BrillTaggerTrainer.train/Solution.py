import nltk
from nltk.tag import UnigramTagger, BigramTagger, brill, brill_trainer
from nltk.corpus import treebank

# Assuming train_sents is already defined and is a list of sentences with tagged words
# train_sents = [[('The', 'DT'), ('cat', 'NN'), ...], ...]

# Train initial Unigram and Bigram Taggers
unigram_tagger = UnigramTagger(train_sents)
bigram_tagger = BigramTagger(train_sents, backoff=unigram_tagger)

# Define Brill Tagger Templates
templates = brill.fntbl37()

# Set parameters
max_rules = 100  # max number of transformations
min_score = 2    # minimum score improvement
min_ac = 0.9     # minimum accuracy as a fraction

# Train Brill Tagger
brill_tagger = brill_trainer.BrillTaggerTrainer(initial_tagger=bigram_tagger, templates=templates, trace=3)
trained_brill_tagger = brill_tagger.train(train_sents, max_rules=max_rules, min_score=min_score)

# Note: No specific parameter for min accuracy in the trainer, it's typically handled by evaluating 
# and selecting the tagger with your desired accuracy post training.

# To test the accuracy on test_sents (list of tagged sentences)
# test_sents = [[('The', 'DT'), ('dog', 'NN'), ...], ...]
# accuracy = trained_brill_tagger.evaluate(test_sents)
# print(f"Accuracy: {accuracy*100:.2f}%")
