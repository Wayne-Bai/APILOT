
import nltk
from nltk.tokenize import TreebankWordTokenizer

def detokenize(tokens):
    detokenizer = TreebankWordTokenizer()
    text = detokenizer.detokenize(tokens)
    return text

# Example usage
tokens = ["Hello", ",", "how", "are", "you", "?"]
detokenized_text = detokenize(tokens)
print(detokenized_text)
