from textblob import TextBlob

def analyze_sentiment(text):

    blob = TextBlob(text)
    score = blob.sentiment.polarity
    confidence = abs(score)


    
    if score > 0.1:
        tag = 'positive'
    elif score < -0.1:
        tag = 'negative'
    else:
        tag = 'neutral'

    return {
        'sentiment': tag,
        'confidence': confidence
    }

