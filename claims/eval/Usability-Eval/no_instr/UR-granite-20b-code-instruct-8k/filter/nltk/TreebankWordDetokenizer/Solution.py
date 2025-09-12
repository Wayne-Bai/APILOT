import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer

# Example text to detokenize
text = "This is an example text for detokenizing."

# Create a TreebankWordDetokenizer object
detokenizer = TreebankWordDetokenizer()

# Detokenize the text
detokenized_text = detokenizer.detokenize(text.split())

# Print the detokenized text
print(detokenized_text)
