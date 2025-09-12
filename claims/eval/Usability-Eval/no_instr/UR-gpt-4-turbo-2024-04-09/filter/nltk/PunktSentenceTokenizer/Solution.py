import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktTrainer

text = """
Your large block of text here.
Replace this string with actual text to enable the tokenizer to learn from it.
"""

# Create a new Punkt trainer
trainer = PunktTrainer()
trainer.INCLUDE_ALL_COLLOCS = True
trainer.train(text)

# Create the tokenizer with the trained model
tokenizer = PunktSentenceTokenizer(trainer.get_params())

# Test the tokenizer on some new text
test_text = "This is a test text. It should correctly identify sentence boundaries! Is it working well? Let's hope so."
sentences = tokenizer.tokenize(test_text)

for sentence in sentences:
    print(sentence)
