import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer

# Sample tokenized text
tokenized_text = ['I', 'am', 'a', 'coding', 'expert']

# Creating an instance of TreebankWordDetokenizer
detokenizer = TreebankWordDetokenizer()

# Detokenizing the text
detokenized_text = detokenizer.detokenize(tokenized_text)

print("Detokenized text: ", detokenized_text)
