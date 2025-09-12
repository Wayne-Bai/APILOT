
import re

# Custom tokenizer for tweets
def tweet_tokenizer(text):
    # Remove usernames starting with @
    text = re.sub(r'@[A-Za-z0-9_]+', '', text)
    # Remove hashtags starting with #
    text = re.sub(r'#', '', text)
    
    # Split the text into tokens
    tokens = text.split()
    
    return tokens

# Test the tokenizer
tweet = "Excited to start coding with @nltk! #Python #NLP"
tokens = tweet_tokenizer(tweet)
print(tokens)
