from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

# Sample text for word tokenization
text = "The stars are the streetlights of eternity."

# Tokenizing the text into words
tokens = word_tokenize(text)
print("Word Tokens:", tokens)  # Output the list of word tokens

# Sample text for sentence tokenization
text = """As the sun dipped below the horizon, the sky erupted in a canvas of vibrant colors. 
A gentle breeze carried the scent of blooming flowers, inviting tranquility. 
In that moment, everything felt possible, and hope danced on the edge of twilight."""

# Tokenizing the text into sentences
tokens = sent_tokenize(text)
print("Sentence Tokens:", tokens)  # Output the list of sentence tokens

# Challenge for students:
# Now, try to tokenize the first text by individual characters.
# Hint: You can use a simple list comprehension or the built-in 'list()' function.

text = "Another random phrase"
char_tokens = text  # Modify this line of code
print("Character Tokens:", char_tokens) 
