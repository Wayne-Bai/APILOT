import nltk
from nltk import TreebankTokenizer, TreebankDetokenizer

def treebank_detokenize(tokens):
    # Create a TreebankTokenizer object and use it to tokenize the input string
    t = TreebankTokenizer()
    tokens = t.tokenize(tokens)

    # Create a TreebankDetokenizer object and use it to detokenize the tokenized string
    dt = TreebankDetokenizer()
    return dt.detokenize(tokens)
