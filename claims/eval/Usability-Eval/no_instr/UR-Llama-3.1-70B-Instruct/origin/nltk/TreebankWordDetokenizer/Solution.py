import nltk
from nltk.tokenize.treebank import TreebankDetokenizer

def detokenize_tokenized_text(tokenized_text):
    """
    Detokenizes a list of words.
    
    Args:
    detokenize_tokenized_text(['This', 'is', 'a','sentence', '.'])
    'This is a sentence.'
    """
    detokenizer = TreebankDetokenizer()
    return detokenizer.detokenize(tokenized_text)

# Example usage
if __name__ == "__main__":
    # Tokenized text
    tokenized_text = ['This', 'is', 'a','sentence', '.']
    
    # Detokenize
    detokenized_text = detokenize_tokenized_text(tokenized_text)
    
    # Output
    print(detokenized_text)
