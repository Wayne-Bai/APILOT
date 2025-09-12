
import nltk
from nltk.tokenize import TweetTokenizer

# Define function to perform tokenization
def tokenize_tweets(text):
    # Create an instance of the TweetTokenizer class
    tokenizer = TweetTokenizer()
    
    # Tokenize the text using the TweetTokenizer method
    tokens = tokenizer.tokenize(text)
    
    return tokens
