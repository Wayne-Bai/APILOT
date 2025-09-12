import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer

# Assume that 'text' is a string of tokenized text.
# For example:
text = "This is a tokenized text . It includes punctuation like ' quotes ' , and we want it detokenized."

# Tokenize the text first
tokens = nltk.word_tokenize(text)

# Initialize the detokenizer
detokenizer = TreebankWordDetokenizer()

# Detokenize the text
detokenized_text = detokenizer.detokenize(tokens)

print(detokenized_text)
