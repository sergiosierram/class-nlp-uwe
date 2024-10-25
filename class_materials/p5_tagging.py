# Modified from: https://shariqhameed127.medium.com/pos-parts-of-speech-tagging-nlp-basics-part-5-of-10-1a4a5c1b721c

import spacy
import nltk
from nltk.tokenize import word_tokenize

def pos_tagger_nltk(sentence):
  words = word_tokenize(sentence)
  
  return nltk.pos_tag(words)

sentence = "Cooking is delightful"
print(pos_tagger_nltk(sentence))


def pos_tagger_spacy(sentence):
  nlp = spacy.load("en_core_web_sm")
  doc = nlp(sentence)
  
  return [(token.text, token.pos_) for token in doc]

sentence = "Cooking is delightful"
print(pos_tagger_spacy(sentence))