import nltk
from nltk.tokenize import regexp_tokenize

# Define the Treebank tokenizer's regexes
tokenizer_pattern = r"(\w+|[^\w\s])+"

# Define the reverse regex operations for detokenization
detokenizer_pattern = r"(" + tokenizer_pattern + r")|(" + tokenizer_pattern + r")"

# Define a function to detokenize using the reverse regex operations
def detokenize(tokens):
    return regexp_tokenize(" ".join(tokens), detokenizer_pattern)

# Example usage:
tokens = ["This", "is", "a", "test", "sentence."]
detokenized = detokenize(tokens)
print(detokenized)
