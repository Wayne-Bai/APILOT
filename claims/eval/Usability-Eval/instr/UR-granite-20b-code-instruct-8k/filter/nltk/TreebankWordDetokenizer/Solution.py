import nltk

# Define the Treebank tokenizer's regexes
treebank_regexes = nltk.tokenize.treebank.TB_REGEXES

# Create the reverse regex operations dictionary
reverse_regexes = {v: k for k, v in treebank_regexes.items()}

# Use the reverse regex operations to tokenize the text
text = "This is an example sentence."
tokens = nltk.tokenize. TreebankWordTokenizer(regex_cache=reverse_regexes).tokenize(text)

# Print the tokens
print(tokens)
