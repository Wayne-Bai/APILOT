import nltk
from nltk.tokenize import TreebankWordTokenizer

# Download the Treebank tokenizer if not already downloaded
nltk.download('treebank')

# Initialize the Treebank WordTokenizer
tokenizer = TreebankWordTokenizer()

# Define the detokenizer regexes
detokenizer_regexes = {
    r"\b\w+\b": r" . ",
    r"\b\w+\b": r" . ",
    r"\b\w+\b": r" . ",
    # Add more regexes as needed
}

# Function to detokenize a sentence
def detokenize(sentence):
    tokens = tokenizer.tokenize(sentence)
    detokenized_sentence = ""
    for token in tokens:
        for regex, replacement in detokenizer_regexes.items():
            if re.match(regex, token):
                detokenized_sentence += replacement
                break
        else:
            detokenized_sentence += token
    return detokenized_sentence

# Test the detokenizer
sentence = "This is a sample sentence for detokenization."
print(detokenize(sentence))
