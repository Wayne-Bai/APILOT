import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

# Initialize Punkt parameters
punkt_param = PunktParameters()

# Example abbreviation words
abbreviations = [
    "e.g.", "i.e.", "Dr.", "Mr.", "Mrs.", "Ms.", "Prof.", "etc.", "Jan.", "Feb.", "Mar.",
    "Apr.", "Jun.", "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec.", "Mon.", "Tue.",
    "Wed.", "Thu.", "Fri.", "Sat.", "Sun."
]

# Add abbreviations to the Punkt parameters
punkt_param.abbrev_types = set(abbreviations)

# Initialize the Punkt sentence tokenizer with the custom parameters
sentence_tokenizer = PunktSentenceTokenizer(punkt_param)

# Example text
text = """
This is an example text. It contains abbreviations like e.g., i.e., and Dr. Also, it has dates like Jan. 1, 2023. 
The sentence tokenizer should handle these correctly. For instance, it should recognize that "Dr." is an abbreviation 
and not treat it as the end of a sentence.
"""

# Tokenize the text into sentences
sentences = sentence_tokenizer.tokenize(text)

# Print the sentences
for sentence in sentences:
    print(sentence)
