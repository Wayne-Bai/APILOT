import nltk
from nltk.tokenize import word_tokenize

# Download the required NLTK data
nltk.download('punkt')

# Define a function to tokenize tweets
def tokenize_tweets(tweets):
    # Initialize an empty list to store the tokenized tweets
    tokenized_tweets = []

    # Iterate over each tweet
    for tweet in tweets:
        # Tokenize the tweet using word_tokenize
        tokens = word_tokenize(tweet)

        # Append the tokenized tweet to the list
        tokenized_tweets.append(tokens)

    # Return the list of tokenized tweets
    return tokenized_tweets
