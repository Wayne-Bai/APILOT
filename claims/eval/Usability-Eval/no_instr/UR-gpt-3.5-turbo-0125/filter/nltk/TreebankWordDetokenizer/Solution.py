
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer

tokens = ['Hello', ',', 'how', 'are', 'you', '?']
detokenizer = TreebankWordDetokenizer()
detokenized_text = detokenizer.detokenize(tokens)
print(detokenized_text)
