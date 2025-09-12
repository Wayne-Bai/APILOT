import nltk
from nltk.tokenize import TreebankWordTokenizer

def detokenize(sentence):
    tokenizer = TreebankWordTokenizer()
    tokens = tokenizer.tokenize(sentence)
    detokenized_sentence = ' '.join(tokens)
    return detokenized_sentence

# Example usage
sentence = 'The quick brown fox jumps over the lazy dog'
detokenized = detokenize(sentence)
print(detokenized)
