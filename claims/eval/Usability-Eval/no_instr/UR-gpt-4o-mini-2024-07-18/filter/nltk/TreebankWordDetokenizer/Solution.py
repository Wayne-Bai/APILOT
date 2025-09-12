import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer

# Sample tokenized sentences
tokenized_sentences = ["This", "is", "a", "sentence", ".", "Here", "is", "another", "one", "."]

# Detokenize the sentence
detokenizer = TreebankWordDetokenizer()
detokenized_sentence = detokenizer.detokenize(tokenized_sentences)

print(detokenized_sentence)
