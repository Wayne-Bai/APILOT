import nltk
from nltk.tokenize import regular_expression_tokenizer

# Define the regex patterns for tokenization
WORD_SPLIT = re.compile(r'\W+')
SPACE_SPLIT = re.compile(r'[\s]+')

# Define the reverse regex operations for detokenization
DETOKENIZE_REGEX = re.compile(r'\s*(\w[\w\']*)\s*')

def detokenize(tokens):
    return DETOKINKZE_REGEX.sub(' ', ' '.join(tokens)).strip()

# Test the function
tokens = ['This', 'is', 'a', 'test', 'string']
print(detokenize(tokens))
