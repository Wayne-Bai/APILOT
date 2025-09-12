import nltk
from nltk.tokenize import word_tokenize

# Download the required NLTK data
nltk.download('punkt')

# Define a function to tokenize tweets
def tokenize_tweets(tweets):
    return [word_tokenize(tweet) for tweet in tweets]
