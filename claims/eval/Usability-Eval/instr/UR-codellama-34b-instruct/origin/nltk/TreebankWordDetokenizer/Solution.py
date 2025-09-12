
import nltk
from nltk.tokenize import TreebankWordTokenizer

# Tokenize some text using the Treebank tokenizer
tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize("This is a test sentence.")

# Use the reverse regex operations to detokenize the tokens
detokenizer = TreebankWordDetokenizer()
text = detokenizer.detokenize(tokens)

print(text) # Output: This is a test sentence.
