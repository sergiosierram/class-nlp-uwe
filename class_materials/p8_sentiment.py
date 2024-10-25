# Taken from: https://medium.com/@mail4sameera/sentiment-analysis-nlp-understanding-emotions-in-text-data-a9dfa39db2de

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Sample text
text = "I absolutely love this product! It exceeded my expectations."

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Get sentiment scores
sentiment_scores = sia.polarity_scores(text)

# Interpret sentiment scores
if sentiment_scores['compound'] >= 0.05:
    sentiment = "Positive"
elif sentiment_scores['compound'] <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print("Text to analyze: {0}\n".format(text))
print(f"The sentiment of the text is: {sentiment}")

# Try changing the original text!