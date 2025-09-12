import nltk
from nltk.tag import brill, brill_trainer
from nltk.tag import RegexpTagger

# Example train_sents corpus
train_sents = [
    [('The', 'DT'), ('cat', 'NN'), ('sat', 'VBD'), ('on', 'IN'), ('the', 'DT'), ('mat', 'NN')],
    [('She', 'PRP'), ('bought', 'VBD'), ('some', 'DT'), ('apples', 'NNS')],
    # Add more sentences as needed
]

# Define a baseline tagger (e.g., RegexpTagger)
baseline_tagger = RegexpTagger([
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
    (r'(The|the|A|a|An|an)$', 'DT'),  # articles
    (r'.*able$', 'JJ'),  # adjectives
    (r'.*ness$', 'NN'),  # nouns formed from adjectives
    (r'.*ly$', 'RB'),  # adverbs
    (r'.*s$', 'NNS'),  # plural nouns
    (r'.*', 'NN')  # nouns (default)
])

# Define the Brill template
templates = [
    brill.Template(brill.Pos([-1])),
    brill.Template(brill.Pos([1])),
    brill.Template(brill.Word([-1])),
    brill.Template(brill.Word([1])),
    brill.Template(brill.Word([-1]), brill.Pos([-1])),
    brill.Template(brill.Word([1]), brill.Pos([1])),
]

# Train the Brill tagger
max_rules = 10
min_score = 2
min_acc = 0.7

brill_tagger = brill_trainer.BrillTaggerTrainer(baseline_tagger, templates, trace=3)
trained_tagger = brill_tagger.train(train_sents, max_rules=max_rules, min_score=min_score, min_acc=min_acc)

# Output the trained tagger
print(trained_tagger)
