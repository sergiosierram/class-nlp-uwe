# Taken from: https://shariqhameed127.medium.com/text-normalization-nlp-basics-part-4-of-10-a2d15c3754dc

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
 
stemmer = PorterStemmer()
 
sentence = "The quick brown foxes are jumping over the lazy dogs"
words = word_tokenize(sentence)
 
for word in words:
    print(word, ": ", stemmer.stem(word))