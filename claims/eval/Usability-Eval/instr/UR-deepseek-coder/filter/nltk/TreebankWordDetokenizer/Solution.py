import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer

# Example tokenized text
tokenized_text = ["This", "is", "a", "tokenized", "sentence", "."]

# Initialize the TreebankWordDetokenizer
detokenizer = TreebankWordDetokenizer()

# Detokenize the text
detokenized_text = detokenizer.detokenize(tokenized_text)

print(detokenized_text)
