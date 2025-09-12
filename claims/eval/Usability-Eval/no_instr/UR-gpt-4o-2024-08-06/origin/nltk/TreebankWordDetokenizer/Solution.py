import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer

# You can install NLTK using: pip install nltk
# Also make sure to download the necessary NLTK data files if you haven't:
# nltk.download('punkt')

def detokenize(words):
    detokenizer = TreebankWordDetokenizer()
    return detokenizer.detokenize(words)

# Example usage
tokenized_sentence = ['This', 'is', 'a', 'detokenized', 'sentence', '.', 'Let', "'", 's', 'see', 'how', 'it', 'works', '.']
detokenized_sentence = detokenize(tokenized_sentence)
print(detokenized_sentence)
