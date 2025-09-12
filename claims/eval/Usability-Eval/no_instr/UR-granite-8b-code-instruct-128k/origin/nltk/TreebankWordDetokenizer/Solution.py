import nltk
nltk.download('treebank')
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import TreebankDetokenizer
tokenizer = TreebankWordTokenizer()
detokenizer = TreebankDetokenizer()
text = "This is a test sentence."
tokens = tokenizer.tokenize(text)
detokens = detokenizer.detokenize(tokens)
print(detokens)