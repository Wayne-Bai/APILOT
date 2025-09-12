import nltk
from nltk.tokenize import word_tokenize
import re

def tweet_tokenizer(tweet):
    # Clean the tweet by removing links and usernames
    tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
    tweet = re.sub(r'@\w+', '', tweet)
    
    # Tokenize the tweet
    tokens = word_tokenize(tweet)
    
    # Optionally: Remove punctuation and convert to lowercase
    tokens = [word.lower() for word in tokens if word.isalnum()]
    
    return tokens

# Example usage
tweet_example = "Hey @user, check out this link: https://example.com! #exciting"
tokens = tweet_tokenizer(tweet_example)
print(tokens)
