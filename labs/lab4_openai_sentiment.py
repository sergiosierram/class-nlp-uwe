import openai

# Set your OpenAI API key
openai.api_key = 'YOUR-API-KEY'  # Replace with your actual API key

def analyze_sentiment(text):
    try:
        # Call the OpenAI API for sentiment analysis
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Analyze the sentiment of this text: '{text}'"}
            ]
        )
        
        # Extract sentiment from the response
        sentiment = response.choices[0].message.content
        return sentiment
    
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Sample texts for sentiment analysis
    sample_texts = [
        "I love this product! It's amazing.",
        "I'm really disappointed with the service.",
        "It's an okay experience, nothing special.",
        "What a wonderful day! I feel so happy.",
        "I'm not sure how I feel about this."
    ]
    
    # Analyze sentiment for each sample text
    for text in sample_texts:
        sentiment = analyze_sentiment(text)
        print(f"Text: {text}\nSentiment: {sentiment}\n")

if __name__ == "__main__":
    main()
