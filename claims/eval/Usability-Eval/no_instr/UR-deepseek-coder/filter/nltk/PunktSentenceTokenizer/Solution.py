import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

# Initialize Punkt parameters
punkt_param = PunktParameters()

# Example abbreviation words
abbreviations = ['e.g', 'Dr', 'Mr', 'Mrs', 'Ms', 'Prof', 'etc']
punkt_param.abbrev_types = set(abbreviations)

# Initialize the Punkt sentence tokenizer with the custom parameters
sentence_tokenizer = PunktSentenceTokenizer(punkt_param)

# Example text
text = "Mr. Smith bought cheapshoes.com for 13 million dollars, i.e. he paid a lot for it. Dr. Johnson will be presenting his findings on Friday."

# Tokenize the text into sentences
sentences = sentence_tokenizer.tokenize(text)

# Print the sentences
for sentence in sentences:
    print(sentence)
