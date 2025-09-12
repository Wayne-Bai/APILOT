import nltk
from nltk.tokenize import TreebankWordTokenizer

def detokenize(tokens):
    # Initialize a TreebankWordTokenizer
    tokenizer = TreebankWordTokenizer()
    
    # Join tokens into a string
    return ' '.join(tokens)

# Example usage
tokens = ["They", "have", "a", "dog", "."]
detokenized_text = detokenize(tokens)
print(detokenized_text)
