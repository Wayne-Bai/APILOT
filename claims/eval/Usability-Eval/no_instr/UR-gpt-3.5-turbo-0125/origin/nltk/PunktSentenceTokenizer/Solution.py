
import re
from nltk.tokenize import regexp_tokenize

def custom_sentence_tokenizer(text):
    # Define the regex pattern for tokenizing
    pattern = r'''(?x)    # set flag to allow verbose regexps
    (?:[A-Z]\.)+        # abbreviations, e.g. U.S.A.
    | \w+(?:-\w+)*        # words with optional internal hyphens
    | \$?\d+(?:\.\d+)?%?  # currency and percentages
    | \.\.\.            # ellipsis
    | [][.,;"'?():-_`]
    '''
    
    # Tokenize the text using the custom regex pattern
    tokens = regexp_tokenize(text, pattern)
    
    sentences = []
    current_sentence = []
    abbreviations = set(['mr', 'mrs', 'ms', 'dr'])
    
    for token in tokens:
        if token.lower() in abbreviations:
            current_sentence.append(token)
        elif token in ['.']:
            current_sentence.append(token)
            sentences.append(current_sentence)
            current_sentence = []
        else:
            current_sentence.append(token)
    
    # Join the tokens back into sentences
    result = [' '.join(sentence) for sentence in sentences]
    
    return result

# Example usage
text = "Mr. John Doe is a Ph.D. in linguistics. He works at XYZ Inc. This is a test sentence. Another sentence follows."
sentences = custom_sentence_tokenizer(text)
for sentence in sentences:
    print(sentence)
