import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def tweet_tokenizer(tweet):
    # Convert tweet to lowercase
    tweet = tweet.lower()

    # Tokenize the tweet into words
    words = word_tokenize(tweet)

    # Remove punctuation from tokenized words
    words = [word for word in words if word.isalnum()]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    return words

# Example usage
tweet = "Here's to the crazy ones: the misfits, the rebels, the troublemakers, 😀 and more!"
tokens = tweet_tokenizer(tweet)
print(tokens)
