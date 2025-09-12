import nltk
from nltk.tokenize import TweetTokenizer

# Download the punkt tokenizer for English
nltk.download('punkt')

# Initialize the TweetTokenizer
tokenizer = TweetTokenizer()

# Example usage
tweet = "Hello, this is an example tweet! #nltk #python"
tokens = tokenizer.tokenize(tweet)
print(tokens)
