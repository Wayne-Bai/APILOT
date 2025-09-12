import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer

# Example tokens to detokenize
tokens = ['This', 'is', "n't", 'an', 'example', '.']

# Initialize the TreebankWordDetokenizer
detokenizer = TreebankWordDetokenizer()

# Detokenize the list of words
detokenized_text = detokenizer.detokenize(tokens)

print(detokenized_text)
