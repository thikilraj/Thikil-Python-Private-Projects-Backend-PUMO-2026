from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Create sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Get user input
text = input("Enter a sentence: ")

# Analyze sentiment
score = analyzer.polarity_scores(text)
compound_score = score["compound"]

# Determine sentiment
if compound_score >= 0.05:
    sentiment = "Positive"
elif compound_score <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

# Display output
print("\n--- Sentiment Analysis Result ---")
print("Text:", text)
print("Sentiment:", sentiment)
print("Compound Score:", compound_score)