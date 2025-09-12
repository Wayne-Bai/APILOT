import re
from nltk.tokenize.treebank import TreebankWordDetokenizer

# Initialize the Treebank detokenizer
detokenizer = TreebankWordDetokenizer()

# Example tokenized text
tokenized_text = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "."]

# Detokenize the text
detokenized_text = detokenizer.detokenize(tokenized_text)

print(detokenized_text)
