import re

def clean_text(text):
    """
    Cleans raw tweet text for NLP processing
    """

    # Convert to lowercase
    text = text.lower()

    # Remove retweet marker
    text = re.sub(r'^rt\s+', '', text)

    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # Remove mentions (@username)
    text = re.sub(r'@\w+', '', text)

    # Remove hashtags (#word)
    text = re.sub(r'#\w+', '', text)

    # Remove emojis and special characters
    text = re.sub(r'[^a-z\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text
