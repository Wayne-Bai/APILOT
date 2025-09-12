import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer

# Example tokenized text
tokenized_text = ['This', 'is', 'an', 'example', '.', 'Can', 'you', 'detokenize', 'this', '?']

# Create a detokenizer instance
detokenizer = TreebankWordDetokenizer()

# Detokenize the tokenized text
detokenized_text = detokenizer.detokenize(tokenized_text)

print(detokenized_text)
