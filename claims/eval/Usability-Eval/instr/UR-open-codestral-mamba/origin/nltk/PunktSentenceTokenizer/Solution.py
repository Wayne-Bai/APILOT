import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def tokenize_sentences(text):
    return sent_tokenize(text)

# Test
text = "Hello World! How are you? I hope you're doing well. Thank you!"
sentences = tokenize_sentences(text)
for sentence in sentences:
    print(sentence)
