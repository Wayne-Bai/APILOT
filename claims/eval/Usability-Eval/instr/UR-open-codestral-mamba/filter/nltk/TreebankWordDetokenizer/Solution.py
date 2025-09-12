import nltk
from nltk.tokenize import TreebankWordDetokenizer

# List of tokens
tokens = ['I', 'go', 'to', 'school', 'by', 'bus']

# Create an instance of TreebankWordDetokenizer
detokenizer = TreebankWordDetokenizer()

# Use the detokenize method to convert list of tokens back to a string
sentence = detokenizer.detokenize(tokens)

print(sentence)
